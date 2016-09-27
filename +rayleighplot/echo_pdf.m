function pdf = echo_pdf(amplitude, thermal_noise_power)
%ECHO_PDF Returns a PDF of a radar echo based on wave amplitude and thermal
% noise power
    pdf =  @(envelope): ((envelope ./ thermal_noise_power) .* ...
                             exp(-(envelope.^2 + amplitude.^2) ./ (2 .* thermal_noise_power)) .* ...
                            besseli(0, (envelope .* amplitude) ./ thermal_noise_power));
end

