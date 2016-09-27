function thresh = threshold(probability_false_alarm, thermal_noise_power)
%THRESHOLD Computes voltage threshold from probability of false alarm.
    thresh = sqrt(-2 .* 50 .* thermal_noise_power .* ...
                log(probability_false_alarm));
end

