//IFDEF OPENACC

    double lambda, mu, rho, grav, d, r, LDratio, Area, alphaM;
    double h;
    double tract, normR;
    double K_temp, K_total, F_S_temp, F_S_total;

//ENDIF
    
    int numips, nstress, nisv, ndof, nel, neldof;
    int nsteps, print_int, n_print;
    int ii, jj, kk, ll, n, el, ip;
    int I, J;
    int Rtol;
    int numtasks, rank, rc;

//IFDEF OPENACC
    
    string dirName, dirPrefix;

//ENDIF
