library(testthat)
source('temporal_overlap_probability.R')

test_that("get_annual_cost returns cost within 5% of the target", {
    set.seed(333)

    # target = days * prob * cost per downtime.
    target <- 365 * .3682 * 1000  # prob calculated with seed 42.

    # assert the returned value is within the 5% variation threshold for 100 runs
    for (i in 1:100) {
        expect_true(
            (get_annual_cost(1000, 60, 300) - target) < (target * 0.05)
        )
    }
})
