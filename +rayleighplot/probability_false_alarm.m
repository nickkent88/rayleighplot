function Pfa = probability_false_alarm(envelope, thermal_noise_power)
% PROBABILITY_FALSE_ALARM Computes probability of false alarm based on a
% particular voltage threshold and thermal noise power.
    Pfa = exp(-(envelope.^2) / (2 .* thermal_noise_power));
end

