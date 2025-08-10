function bestParams = run_optimization(cstProject)
    numVars = 3;  % 최적화할 변수 개수
    lb = [16, 18, 40];  % 하한값
    ub = [26, 22, 90];  % 상한값

    options = optimoptions('ga', ...
    'PopulationSize', 50, ...
    'MaxGenerations', 100, ...
    'MutationFcn', {@mutationadaptfeasible, 0.1}, ... % mutationadaptfeasible로 변경
    'CrossoverFraction', 0.8, ...
    'Display', 'iter', ...
    'PlotFcn', @gaplotbestf);

    % cstProject를 objective_function에 전달할 수 있도록 함수 핸들 생성
    costFunction = @(params) objective_function(cstProject, params);

    % GA 실행
    bestParams = ga(costFunction, numVars, [], [], [], [], lb, ub, [], options);

    disp('optimized values:');
    disp(bestParams);
end
