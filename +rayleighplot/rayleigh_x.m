function x_rayleigh = rayleigh_x(probability, porigin)
%RAYLEIGH_X Converts x-coordinates to rayleigh plot coordinates.

    x_rayleigh = (10.0 .* log10(-log(probability_at_origin)) - ...
                  10.0 .* log10(-log(probability)));


end

