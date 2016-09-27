function y_rayleigh = rayleigh_y(amplitude)
%RAYLEIGH_Y Converts y-coordinates to rayleigh plot coordinates.

    y_rayleigh = 10.0 .* log10(amplitude.^2);
end

