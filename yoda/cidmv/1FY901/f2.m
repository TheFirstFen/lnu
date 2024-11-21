function dxdt = f2(t,x)
  k=0.1;
  m=1.0;

dxdt=[x(2);-(k./m).*x(1)];
