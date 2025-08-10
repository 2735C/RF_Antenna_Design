function cstProject = open_cst_project(cstFilePath)
    cst = actxserver('CSTStudio.application');  % CST 실행
    cstProject = invoke(cst, 'OpenFile', cstFilePath);  % CST 프로젝트 열기

    % 현재 활성화된 프로젝트 가져오기
      

    disp('CST is open.');
end
