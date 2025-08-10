function [result1, result2, result3] = run_cst_simulation(cstProject, params)
    % CST 변수 확인
    disp(cstProject);

    disp(['ellip_r_max: ', num2str(params.ellip_r_max)]);
    disp(['hole_r: ', num2str(params.hole_r)]);
    disp(['ref_gap: ', num2str(params.ref_gap)]);

    a = num2str(params.ellip_r_max);
    b = num2str(params.hole_r);
    c = num2str(params.ref_gap);

    % CST 변수 업데이트
    invoke(cstProject, 'StoreParameter', 'ellip_r_max', a);
    invoke(cstProject, 'StoreParameter', 'hole_r', b);
    invoke(cstProject, 'StoreParameter', 'ref_gap', c);
    invoke(cstProject, 'Rebuild');

    % CST 시뮬레이션 실행
    solver = invoke(cstProject, 'Solver');
    invoke(solver, 'Start');
    pause(400);
    disp(cstProject);

    fclose('all'); 
    % Directivity 결과 가져오기
    fid = fopen('D:\eunjijung\mail_for_Empire\directivity.txt', 'r'); % 파일 열기 (읽기 모드)
    directivity = fscanf(fid, '%f');   % 파일에서 숫자 읽기
    result2 = directivity(1);  % 첫 번째 값이 Directivity라고 가정
    disp(['Directivity: ', num2str(result2)]);
    fclose(fid);

    % n_parallel 결과 가져오기
    fid = fopen('D:\eunjijung\mail_for_Empire\n_parallel.txt', 'r'); % 파일 열기 (읽기 모드)
    n_parallel = fscanf(fid, '%f');   % 파일에서 숫자 읽기
    result3 = n_parallel(1);
    disp(['n_parallel: ', num2str(result3)]);
    fclose(fid);                  % 파일 닫기
    %S11 가져오기
    % 파일 경로
    S11FilePath = 'D:\eunjijung\CST\Combline_sample\Export\Matlab_S11_S-Parameters-S1,1.txt';

    % 파일 열기
    fid = fopen(S11FilePath, 'r');  % 읽기 모드로 파일 열기
    if fid == -1
    error('파일을 열 수 없습니다.');
    end

    % 파일 내용 읽기
    found = false;  % 조건에 맞는 데이터가 있는지 체크
    result1 = NaN;  % S11 절댓값을 저장할 변수

    while true
        % 한 줄씩 읽기
        line = fgetl(fid);  
        if ~ischar(line)
            break;  % 파일 끝
        end
    
        % 공백을 기준으로 숫자 분리
        data = str2double(strsplit(line)); 
    
        % 첫 번째 열이 476.0 (4.7600000E+02)인지 확인
        if abs(data(1) - 476.0) == 0  % 476.0 근처에서 찾기
            % 두 번째 열(실수부)와 세 번째 열(허수부)
            real_part = data(2);  % 실수부
            imag_part = data(3);  % 허수부
            
            % S11 절댓값 계산
            result1 = sqrt(real_part^2 + imag_part^2);  
            found = true;  % 조건에 맞는 데이터를 찾았음
            break;  % 더 이상 읽을 필요 없음
        end
    end

    fclose(fid);  % 파일 닫기
    
    % 결과 출력
    if found
        disp(['S11_abs at 476.0 MHz ', num2str(result1)]);
        
    else
        disp('476.0 MHz에 해당하는 데이터가 파일에 없습니다.');
    end

end
