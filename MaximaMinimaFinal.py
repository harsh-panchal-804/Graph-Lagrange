def multi():
    try:
        import sympy as sym
        from sympy import plotting
        p = sym.symbols('x')  # Real =true will only give real and not complex values of x
        q = sym.symbols('y')
        lmbda = sym.symbols('lambda')

        print("=" * 60)
        print("          MULTIVARIABLE FUNCTION ANALYSIS (2D)")
        print("=" * 60)

        function_str = input("Enter the 2D function f(x, y) (e.g., x**4 + y**4 - 4*x*y + 1): ")
        polf = sym.sympify(function_str)

        print("\n[ FUNCTION ]")
        print(f"f(x, y) = {polf}")
        print("=" * 60)

        dfx = sym.diff(polf, p)
        dfy = sym.diff(polf, q)
        result = sym.solve([dfx, dfy], (p, q))  # All the points of possible maxima/minima
        # We use sy.solve instead of sym.evaluate as simultaneous equations will not be solved by the latter
        print("[ UNCONSTRAINED CRITICAL POINTS ]")
        print(f"Points (∇f = 0): {result}")

        # Now we calculate Hessian
        dfx2 = sym.diff(dfx, p)
        dfy2 = sym.diff(dfy, q)
        dfxy = sym.diff(dfx, q)

        Hessian = sym.Matrix([[dfx2, dfxy], [dfxy, dfy2]])
        print("\n[ HESSIAN MATRIX ]")
        print("H = ")
        print(Hessian)

        if not isinstance(result, list):
            result = [result]

        x_min, x_max = 0, 0
        y_min, y_max = 0, 0

        print("\n" + "=" * 60)
        print("       SECOND DERIVATIVE TEST (EXTREMA CLASSIFICATION)")
        print("=" * 60)
        print("CRITICAL POINT | H1 (dfxx) | H2 (Det) | CLASSIFICATION | f(x, y) VALUE")
        print("-" * 85)

        for point in result:  # Now we put values in all differentiations

            if isinstance(point, dict):
                sub = point
            else:
                sub = {p: point[0], q: point[1]}

            try:
                x_val = float(sym.N(sub[p]))
                y_val = float(sym.N(sub[q]))
                x_min = min(x_min, x_val)
                x_max = max(x_max, x_val)
                y_min = min(y_min, y_val)
                y_max = max(y_max, y_val)
            except (TypeError, ValueError):
                pass

            dfx2a = dfx2.evalf(subs=sub)
            dfy2a = dfy2.evalf(subs=sub)
            dfxya = dfxy.evalf(subs=sub)
            h2 = dfx2a * dfy2a - (dfxya ** 2)  # Calculating H2
            h1 = dfx2a  # Calculating H1
            f_val = polf.evalf(subs=sub)

            point_str = f"({sym.N(sub[p], 3):.3f}, {sym.N(sub[q], 3):.3f})"
            h1_str = f"{sym.N(h1):.4f}"
            h2_str = f"{sym.N(h2):.4f}"
            f_val_str = f"{sym.N(f_val):.4f}"

            classification = "Inconclusive"
            if h2 < 0:
                classification = "SADDLE POINT"
            elif h2 > 0:
                if h1 > 0:
                    classification = "LOCAL MINIMA"
                elif h1 < 0:
                    classification = "LOCAL MAXIMA"

            print(
                f"{point_str.ljust(15)} | {h1_str.ljust(9)} | {h2_str.ljust(8)} | {classification.ljust(14)} | {f_val_str}")

        print("-" * 85)

        # --- ENHANCEMENT: LAGRANGE MULTIPLIERS (CONSTRAINED OPTIMIZATION) ---

        use_lagrange = input(
            "\nDo you want to compute constrained extrema using Lagrange Multipliers (g(x, y) = 0)? (y/n): ").lower()
        if use_lagrange == 'y':
            g_str = input("Enter the constraint function g(x, y) (e.g., x + y - 1): ")
            try:
                g = sym.sympify(g_str)

                Lagrangian = polf - lmbda * g

                dLdx = sym.diff(Lagrangian, p)
                dLdy = sym.diff(Lagrangian, q)
                # dL/dlambda = 0 gives back the constraint g=0

                lagrange_result = sym.solve([dLdx, dLdy, g], (p, q, lmbda))

                if not isinstance(lagrange_result, list):
                    lagrange_result = [lagrange_result]

                print("\n" + "=" * 60)
                print("      LAGRANGE MULTIPLIERS (CONSTRAINED EXTREMA)")
                print("=" * 60)
                print("x | y | lambda | f(x, y) VALUE")
                print("-" * 50)

                for point in lagrange_result:

                    if isinstance(point, dict):
                        sub = point
                    else:
                        sub = {p: point[0], q: point[1], lmbda: point[2]}

                    x_val = sym.N(sub[p])
                    y_val = sym.N(sub[q])
                    lmbda_val = sym.N(sub[lmbda])

                    f_val_lagrange = polf.evalf(subs={p: x_val, q: y_val})

                    try:
                        x_min = min(x_min, float(x_val))
                        x_max = max(x_max, float(x_val))
                        y_min = min(y_min, float(y_val))
                        y_max = max(y_max, float(y_val))
                    except (TypeError, ValueError):
                        pass

                    print(
                        f"{sym.N(x_val):.4f} | {sym.N(y_val):.4f} | {sym.N(lmbda_val):.4f} | {sym.N(f_val_lagrange):.4f}")
                print("-" * 50)

            except Exception as e:
                print(f"\n[ LAGRANGE ERROR ] Could not solve constraint: {e}")

        # --- PLOTTING ---

        plt = int(input("\nDo you want to plot the function?(1/0): "))
        if plt == 1:
            # Dynamic Plotting Range
            x_range = max(10, x_max - x_min + 5)
            y_range = max(10, y_max - y_min + 5)
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2

            x_start = x_center - x_range / 2
            x_end = x_center + x_range / 2
            y_start = y_center - y_range / 2
            y_end = y_center + y_range / 2

            plotting.plot3d(polf, (p, x_start, x_end), (q, y_start, y_end),
                            title=f"3D Plot of f(x, y) = {polf}",
                            xlabel='X-axis', ylabel='Y-axis', zlabel='f(x, y)',
                            nb_of_points_x=80, nb_of_points_y=80)


    except Exception as e:
        print("\n" + "=" * 60)
        print("ERROR: The Function has Imaginary Minima and Maxima or another issue occurred.")
        print(f"Details: {e}")
        print("=" * 60)
        try:
            plt = int(input("Do you still want to plot the function?(1/0): "))
            if plt == 1:
                plotting.plot3d(polf, (p, -10, 10), (q, -10, 10))
        except:
            pass


typ = int(input("Is your function 2D (1/0): "))


def single():
    try:
        import sympy as sym
        from sympy import plotting
        p = sym.symbols('x')  # Real =true will only give real and not complex values of x

        print("=" * 60)
        print("           SINGLE VARIABLE FUNCTION ANALYSIS (1D)")
        print("=" * 60)

        function_str = input("Enter the 1D function f(x) with parameters (e.g., a*x**3 + b*x + c): ")
        param_str = input("Enter parameter symbols separated by commas (e.g., a, b, c): ")

        param_names = [name.strip() for name in param_str.split(',')]

        params = [sym.symbols(name) for name in param_names]

        polf_symbolic = sym.sympify(function_str)

        while True:
            substitutions = {}
            print("\n" + "#" * 60)
            print("  INTERACTIVE PARAMETER UPDATE (Type 'q' to quit at any time)")
            print("#" * 60)

            try:
                for name in param_names:
                    value = input(f"  Enter value for parameter '{name}': ")
                    if value.lower() == 'q':
                        raise KeyboardInterrupt
                    substitutions[sym.Symbol(name)] = float(value)
            except KeyboardInterrupt:
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                continue

            polf = polf_symbolic.subs(substitutions)

            print("\n[ CURRENT FUNCTION ]")
            print("$$ f(x) = " + sym.latex(polf) + " $$")

            dfx = sym.diff(polf, p)
            dfx2 = sym.diff(dfx, p)

            result = sym.solve([dfx], (p))

            listf = []
            x_min, x_max = 0, 0
            for res in result:
                if isinstance(res, sym.Expr):
                    listf.append(res)

                try:
                    x_val = float(sym.N(res))
                    x_min = min(x_min, x_val)
                    x_max = max(x_max, x_val)
                except (TypeError, ValueError):
                    pass

            print("[ CRITICAL POINTS (df/dx = 0) ]")
            print("-" * 60)
            print("POINT (x) | df^2/dx^2 | CLASSIFICATION | f(x) VALUE")
            print("-" * 60)

            try:
                for i in range(0, len(listf)):
                    point_value = listf[i]

                    dfx2a = dfx2.evalf(subs={p: point_value})

                    classification = "Inconclusive"
                    if dfx2a > 0:
                        classification = "LOCAL MINIMA"
                    elif dfx2a < 0:
                        classification = "LOCAL MAXIMA"

                    ans = polf.subs(p, point_value)

                    x_str = f"{sym.N(point_value):.4f}"
                    dfx2_str = f"{sym.N(dfx2a):.4f}"
                    f_val_str = f"{sym.N(ans):.4f}"

                    print(f"{x_str.ljust(9)} | {dfx2_str.ljust(9)} | {classification.ljust(14)} | {f_val_str}")
                print("-" * 60)

                inflection_result = sym.solve([dfx2], (p))
                inflection_points = []
                for res in inflection_result:
                    if isinstance(res, sym.Expr):
                        inflection_points.append(res)
                        try:
                            x_val = float(sym.N(res))
                            x_min = min(x_min, x_val)
                            x_max = max(x_max, x_val)
                        except (TypeError, ValueError):
                            pass

                print("\n[ INFLECTION POINTS (d^2f/dx^2 = 0) ]")
                if inflection_points:
                    print("-" * 35)
                    print("x | f(x) VALUE")
                    print("-" * 35)
                    for ip in inflection_points:
                        ip_val = polf.subs(p, ip)
                        print(f"{sym.N(ip, 4):.4f} | {sym.N(ip_val, 4):.4f}")
                    print("-" * 35)
                else:
                    print("No Inflection Points found where d^2f/dx^2 = 0.")

                # --- Asymptotic Behavior (Limits) ---
                print("\n[ ASYMPTOTIC BEHAVIOR ]")
                limit_plus = sym.limit(polf, p, sym.oo)
                limit_minus = sym.limit(polf, p, -sym.oo)

                print(f"Limit as x approaches +infinity: {limit_plus}")
                print(f"Limit as x approaches -infinity: {limit_minus}")

                plt = input("\nDo you want to plot the function?(1/0): ")
                if plt == '1':
                    # Dynamic Plotting Range
                    x_range = max(10, x_max - x_min + 5)
                    x_center = (x_min + x_max) / 2
                    x_start = x_center - x_range / 2
                    x_end = x_center + x_range / 2

                    plotting.plot(polf, (p, x_start, x_end),
                                  title=f"Plot of f(x) = {polf}",
                                  xlabel='X-axis', ylabel='f(x)')

            except Exception as e:
                print("\nError during critical point analysis or plotting.")
                print(e)

                try:
                    plt = input("Do you still want to plot the function?(1/0): ")
                    if plt == '1':
                        plotting.plot(polf, (p, -10, 10))
                except:
                    pass

            if input("\nChange parameters and re-analyze? (y/n): ").lower() != 'y':
                break

    except Exception as e:
        print("\n" + "=" * 60)
        print(f"FATAL ERROR during analysis: {e}")
        print("=" * 60)
        # Final plot attempt outside loop if polf exists
        if 'polf' in locals() and input("Attempt final plot? (1/0): ") == '1':
            try:
                plotting.plot(polf, (p, -10, 10))
            except:
                pass


# Sample x^4 +y^4 -4xy +1


# Main
if typ == 1:
    multi()
elif typ == 0:
    single()
else:
    print("Wrong input")
