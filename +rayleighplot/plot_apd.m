function plot_apd(amplitude, probability)
% plots (a,p) pairs representing the APD on Rayleigh graph. %
% input variables:
% a = ordered amplitudes
% p = probability of ordered amplitude
% x-axis labels (labels must be same length)

    xticklabel = {'0.0001', '0.01', '0.1', '1', '5', '10', '20', '30',...
                  '40', '50', '60', '70', '80', '90', '95', '98', '99'};
    ptick = [0.0001 .01 0.1 1 5 10 20 30 40 50 60 70 80 90 95 98 99]/100; 
    porigin = ptick(1);

    % replace 0 valued amplitudes with NaN to avoid logarithm error messages
    if min(amplitude) == 0
        idx = find(amplitude == 0);
        amplitude(idx) = NaN; 
    end

    % replace peak amplitude 0 probability with NaN to avoid logarithmic error messages 
    p(length(amplitude)) = NaN;
    
    % map a and p and plot
    x = 10.0 * log10(-log(porigin)) - 10.0 * log10(-log(probability)); 
    y = 20.0 * log10(amplitude);
    plot(x,y,'LineWidth',2);
    grid
    
    % customize x axis
    xlabel('percent exceeding ordinate');
    xtick = 10.0 * log10(-log(porigin)) - 10.0 * log10(-log(ptick)); 
    xlim([min(xtick) max(xtick)]);
    set(gca,'XTick' ,xtick);
    set(gca,'XTickLabel', xticklabel);
    return