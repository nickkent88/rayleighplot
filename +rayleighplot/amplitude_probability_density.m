function [amplitude, probability] = amplitude_probability_density(s);
% [a, p] = apd(s) estimates the amplitude probability distribution function. %
% input parameters:
% s = amplitude samples %
% return variables:
% a = ordered amplitudes
% p = probability that the ordered ampitude is exceeded
    if isreal(s) & min(s)>=0 amplitude = sort(s);
        N = length(amplitude);
        probability = 1 - [1:N]/N;
    else
        disp('Input values must be amplitudes i.e. real and positive values.');
    end
end