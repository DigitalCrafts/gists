total_outer_loop_iterations = 0
total_inner_loop_iterations = 0

for i in range(0,5):

    print("OUTER LOOP ITERATIONS: %d" % total_outer_loop_iterations)
    
    for j in range(0,3):

        print("inner loop iterations: %d" % total_inner_loop_iterations)
        total_inner_loop_iterations = total_inner_loop_iterations + 1
    
    total_outer_loop_iterations = total_outer_loop_iterations + 1