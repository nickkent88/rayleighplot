function amp = amplitude(snr, thermal_noise_power)
%AMPLITUDE Computes amplitude from desired SNR and thermal noise.
    amp = sqrt(snr .* 2 .* thermal_noise_power);
end

