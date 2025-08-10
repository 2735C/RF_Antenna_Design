clc; clear; close all;

% CST 프로젝트 열기
cstFilePath = 'D:\eunjijung\CST\Combline_sample.cst';
cstProject = open_cst_project(cstFilePath);
pause(15)
% CST에서 변수 로드
cstParams = load_cst_parameters(cstProject);
pause(15)

disp('Variables successfully passed to the main function.');

% GA 최적화 실행
optimalParams = run_optimization(cstProject);
pause(15)
% 최적화된 결과를 CST로 다시 적용
apply_optimized_params_to_cst(cstProject, optimalParams);

disp('optimization complete');
invoke(cstProject, 'Save'); 
invoke(cstProject, 'Quit'); 
 
release(cstProject); 
