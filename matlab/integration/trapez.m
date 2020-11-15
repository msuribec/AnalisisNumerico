function val =trapez(f,a,b)
fa = f(a);
fb = f(b);
val = (b - a) * (fa + fb) / 2;
fprintf('Estimation with trapezoid method = %.15f', val)
end
