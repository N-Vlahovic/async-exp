## Problem Description
We will herein experiment with synchronous requests in an asynchronous setup:

Imagine given a fixed `INPUT_A` one desires to fetch `OUTPUT`, 
where `OUTPUT` is obtained as follows: 

    1. Call ServiceA(INPUT=INPUT_A) --> RESPONSE_A
    2. ProcessServiceAResponse(RESPONSE_A) --> INPUT_B
    3. Call ServiceB(INPUT=INPUT_B) --> RESPONSE_B
    4. ProcessServiceBResponse(RESPONSE_B) --> OUTPUT
    
In other words, a series of *sequential* services need to be called in order
to get `RESPONSE_B` from `INPUT_A` first. Let `FullService` denote the mapping sending
`INPUT_A` to `OUTPUT`.

Besides, imagine this process is to be iterated over a list of initial inputs
`[INPUT_A_1, INPUT_A_2, ..., INPUT_A_N]`. For any two `(INPUT_A_I, INPUT_A_J)`,
the execution of FullService will be independent, i.e. `FullService(INPUT_A_I)`
and `FullService(INPUT_A_J)` can be executed asynchronously.