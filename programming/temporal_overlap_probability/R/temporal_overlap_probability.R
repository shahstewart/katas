get_annual_cost <- function(cost_per_downtime, job_length_in_mins, time_window_in_mins) {
    # let's simulate 10000 starting minutes of the 2 jobs
    n <- 10000
    task1 <- sample.int(time_window_in_mins, size=n, replace=TRUE)
    task2 <- sample.int(time_window_in_mins, size=n, replace=TRUE)
    overlaps <- abs(task1 - task2) <= job_length_in_mins
    overlap_prob <- sum(overlaps) / n

    overlap_prob * 365 * cost_per_downtime
}