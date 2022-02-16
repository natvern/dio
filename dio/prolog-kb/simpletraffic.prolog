atPos(0, 0).
speed(0). 
acc(10).
time(0). 
timestep(1).

nextSpeed(V) :- speed(V1), acc(A),
                timestep(T1),
                V is (V1 + A*T1).

nextPos(X, Y) :- atPos(X1, Y1),
                 speed(V),
                 timestep(T1),
                 X is (X1 + V*T1),
                 Y is (Y1 + V*T1).




