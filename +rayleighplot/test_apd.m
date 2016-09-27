% test_apd
% demonstrates how to use apd(s) and plotapd(a,p).
% ramp
N = 10.0^4;
v = [0:N-1];
[amplitude, probability] = rayleighplot.amplitude_probability_density(abs(v));
rayleighplot.plot_apd(amplitude, probability);
title(sprintf('Simulated ramp, 0-9999 V, N = 10^4, Peak %f dBV',20*log10(amplitude(N)))) 
ylabel('dBV')
pause

%complex Gaussian noise
N = 10.0^6;
v = randn(1,N) + i*randn(1,N);
[amplitude, probability] = rayleighplot.amplitude_probability_density(abs(v));
rayleighplot.plot_apd(amplitude, probability);
title(sprintf('Simulated complex Gaussian noise, variance 2 V^2, N = 10^6, Peak %f V',20*log10(amplitude(N))))
ylabel('dBV')