[input_file, fs] = audioread('recorded file.wav');
x = input_file;

%% Time domain waveform
t = (0:length(x)-1) / fs;  % Time vector (s)
figure;
plot(t, x, 'Color', [0.85, 0.33, 0.1]);
xlabel('Time (s)');
ylabel('Amplitude');
title('Waveform in Time Domain');
grid on;

%% Frequency spectrum (Magnitude)
N = length(x);
f = (0:N-1)*(fs/N);
fft_data = fft(x);
mag = abs(fft_data)/N;

figure;
plot(f(1:floor(N/2)), mag(1:floor(N/2)));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Frequency Spectrum of Input Audio');
grid on;

%% Power Spectrum
power_spectrum = mag.^2;  % Power = |FFT|^2

% Giới hạn tần số từ 0 đến 1000 Hz
f_limit = 1000;
index_limit = find(f <= f_limit);

figure;
plot(f(index_limit), power_spectrum(index_limit));
xlabel('Frequency (Hz)');
ylabel('Power');
title('Power Spectrum of Input Audio (0–1000 Hz)');
grid on;