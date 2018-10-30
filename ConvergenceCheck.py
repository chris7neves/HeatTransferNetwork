def frobenius_norm(tsp, ts, twgp, twg, tcw1p, tcw1, tcw2p, tcw2, tfp, tf, towp, tow, tjp, tj):
    error_ts = ts-tsp
    error_twg = twg - twgp
    error_tcw1 = tcw1 - tcw1p
    error_tcw2 = tcw2 - tcw2p
    error_tfp = tf - tfp
    error_tow = tow - towp
    error_tjp = tj - tjp

    error_squared = (error_ts ** 2) + (error_twg ** 2) + (error_tcw1 ** 2) + (error_tcw2 ** 2) + (error_tfp ** 2) + (error_tow ** 2) + (error_tjp ** 2)

    frobenius_norm_error = (error_squared ** 0.5) / 7

    return frobenius_norm_error
