function [p] = config_ssim(c)
%
% Copyright Aditya Khosla http://mit.edu/khosla
%
% Please cite this paper if you use this code in your publication:
%   A. Khosla, J. Xiao, A. Torralba, A. Oliva
%   Memorability of Image Regions
%   Advances in Neural Information Processing Systems (NIPS) 2012
%

p.grid_spacing = 1; % distance between grid centers
p.Mw = 2; % number of spatial scales for spatial pyramid histogram
p.descriptor = 'ssim';
p.w = 42;

p.pyramid_levels = 2;
p.llcknn = 3;
p.maxsize = 400;

% dictionary parameters
p.dictionary_size = 256;
p.num_images = 500;
p.descPerImage = 2000;
p.num_desc = 500000;

p.train_file = '%s/train_ssim_%d.mat';
p.test_file = '%s/test_ssim_%d.mat';
p.dictionary_file = '%s/dictionary_ssim_%d.mat';

