%
% Copyright Aditya Khosla http://mit.edu/khosla
%
% Please cite this paper if you use this code in your publication:
%   A. Khosla, J. Xiao, A. Torralba, A. Oliva
%   Memorability of Image Regions
%   Advances in Neural Information Processing Systems (NIPS) 2012
%

addpath(genpath(pwd));
addpath utils/libsvm/matlab
addpath matconvnet/matlab
vl_setupnn;
mytraindata=importdata('facePaths-AllTrain.txt');
mytestdata=importdata('facePaths-AllTest.txt');
gendertraindata=importdata('facePaths-AllTrainLabels.txt');
gendertestdata=importdata('facePaths-AllTestLabels.txt');
% Initialize variables for calling datasets_feature function
info = load('images/filelist.mat');
datasets = {'demo14'};
train_lists = {cellstr(mytraindata(1:50))};
test_lists = {cellstr(mytestdata(1:50))};
feature = 'sift';

% Load the configuration and set dictionary size to 20 (for fast demo)
c = conf();
c.feature_config.(feature).dictionary_size=20;

% Compute train and test features
datasets_feature(datasets, train_lists, test_lists, feature, c);

% Load train and test features
%train_features = load_feature(datasets{1}, feature, 'train', c);
%test_features = load_feature(datasets{1}, feature, 'test', c);
train_features = extract_vgg_fc7_features(cellstr(mytraindata(1:50)));
test_features = extract_vgg_fc7_features(cellstr(mytestdata(1:50)));
% Below is a simple nearest-neighbor classifier
%  The display code is more complicated than finding the actual nearest
%  neighbor. Only two lines are required to find the nearest neighbor:
%   [~, nn_idx] = min(sp_dist2(train_features, test_features));
%   predicted_labels = train_labels(nn_idx);
% The images have a border color of black and white to indicate the two
% different classes in the demo dataset.

%
% Display demo images from Stanford Dogs dataset
% URL: http://vision.stanford.edu/aditya86/StanfordDogs/
%

% Display train images in Figure 1
train_labels = transpose(gendertraindata(1:50)); classes = {'Male','Female'};
unique_labels = unique(train_labels);
numPerClass = max(histc(train_labels, unique_labels));
h = figure(1); set(h, 'name', 'Train Images'); border = 10;

for i=1:length(unique_labels)
    idx = find(train_labels==unique_labels(i));
    for j=1:length(idx)
        subplot(length(unique_labels), numPerClass, j+(i-1)*numPerClass);
        im = imread(train_lists{1}{idx(j)});
        im = padarray(im, [border border], 255*(i-1)/(length(unique_labels)-1)); imshow(im); 
        title(sprintf('Example: %d, Class: %s', j, classes{unique_labels(i)}));
    end
end

% Display test images and nearest neighbor from train images in Figure 2
 
test_labels = transpose(gendertestdata(1:50)); classes = {'Male','Female'};
numPerClass = max(histc(test_labels, unique_labels));
h = figure(2); set(h, 'name', 'Test Images'); border = 10;
[~, nn_idx] = min(sp_dist2(train_features, test_features));

for i=1:length(unique_labels)
    idx = find(test_labels==unique_labels(i));
    for j=1:length(idx)
        subplot(length(unique_labels), numPerClass*2, 2*(j-1)+1+(i-1)*numPerClass*2);
        im = imread(test_lists{1}{idx(j)});
        im = padarray(im, [border border], 255*(i-1)/(length(unique_labels)-1)); 
        imshow(im); 
        title(sprintf('Example: %d, Class: %s', j, classes{unique_labels(i)}));
        
        subplot(length(unique_labels), numPerClass*2, 2*(j-1)+2+(i-1)*numPerClass*2);
        im = imread(train_lists{1}{nn_idx(idx(j))}); 
        im = padarray(im, [border border], 255*(train_labels(nn_idx(idx(j)))-1)/(length(unique_labels)-1));
        imshow(im); title(sprintf('Nearest neighbor, predicted class: %s', classes{train_labels(nn_idx(idx(j)))}));
    end
end

%
% Sample code for usage of features with Liblinear SVM classifier:
   C_values = [1e-4 1e-3 1e-2  1e-1 1 10 100 1000 10000];
   %G_values = [1e-4 1e-3 1e-2  1e-1 1 10 100 1000 10000];
   %accuracies=zeros(length(C_values),length(G_values));
   accuracies=zeros(length(C_values),1);
   for i= 1:length(C_values)
        for j = 1:length(G_values)
            %svm_options = ['-s 0 -t 2 -c ' num2str(C_values(i)) ' -g ' num2str(G_values(j))]
            svm_options = ['-s 0 -t 2 -c ' num2str(C_values(i))]
            model = svmtrain(transpose(train_labels), double(train_features), svm_options);
            predicted_labels = svmpredict(transpose(test_labels), sparse(double(test_features)), model);
            accuracies(i) = sum(transpose(test_labels)==predicted_labels)/length(test_labels)
       end
   end
   
  % figure
  % semilogx (C_values, accuracies)
%
