function apply_optimized_params_to_cst(cstProject, params)
    invoke(cstProject, 'StoreParameter', 'ellip_r_max', params(1));
    invoke(cstProject, 'StoreParameter', 'hole_r', params(2));
    invoke(cstProject, 'StoreParameter', 'ref_gap', params(3));
    invoke(cstProject, 'Rebuild');
    
    disp(['Apply optimized values ​​to CST: ', num2str(params)]);
end
