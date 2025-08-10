function cost = objective_function(cstProject, params)
    % params는 double 벡터로 전달됩니다.
    % 이를 구조체로 변환
    paramStruct.ellip_r_max = params(1);
    paramStruct.hole_r = params(2);
    paramStruct.ref_gap = params(3);

    % CST 시뮬레이션 실행 (cstProject도 전달)
    [result1, result2, result3] = run_cst_simulation(cstProject, paramStruct);

    % 목표값 설정
    goal1 = -15;   % S11 값 (s11 < -15)
    goal2 = 60;    % Directivity 값 (directivity > 60)
    goal3 = 3;     % n_parallel 값 (n_parallel = 3)

    % 가중치 설정 (목표 중요도)
    w1 = 1;  % S11 중요도
    w2 = 1;  % Directivity 중요도
    w3 = 5;  % n_parallel 중요도

    % 목적 함수 변환:
    cost = w1 * max(result1 - goal1, 0) + ...
           w2 * max(goal2 - result2, 0) + ...
           w3 * abs(result3 - goal3);  % 비용 함수 정의
end
