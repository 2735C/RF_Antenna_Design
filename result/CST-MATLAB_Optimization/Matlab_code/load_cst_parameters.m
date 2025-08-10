function params = load_cst_parameters(cstProject)

    params.ellip_r_max = 24;
    params.hole_r = 21;
    params.ref_gap = 76;
    invoke(cstProject, 'StoreParameter', 'ellip_r_max', num2str(params.ellip_r_max));
    invoke(cstProject, 'StoreParameter', 'hole_r', num2str(params.hole_r));
    invoke(cstProject, 'StoreParameter', 'ref_gap', num2str(params.ref_gap));

    disp('CST variables loaded completely.');
    disp(['params의 타입: ', class(params)]);

end

