class TimeSeries:
    """ class to generate a timeseries. It can have any or all components of
    - random walk
    - fourier terms (sin)
    - trend, a slow funcition that envlope the others
    """
    
    #########
    def __init__(self, random_walk=True, frourier_term=True, trend=True, length=100):
        # random-walk component         
        self.rw_cmp = rw_generator(N = length)
        # fourier component
        coeffs = coeff_generator(4)
        x = np.linspace(0, 2*np.pi, length)
        self.fr_cmp = periodic_generator(coeffs = coeffs, x=x )
        # trend component
        x = np.linspace(-2, 2,length)
        self.trend_cmp = trend_generator(coeffs = 0.5 - np.random.rand(4), x=x)
        
        self.ts_array = self.rw_cmp + self.fr_cmp + self.trend_cmp

    ##########  
    # random-walk generator
    ##########  
    def rw_generator(N: int, x_0 = 0, p_left=0.5):
        """ generates N steps according to probability to take a step to 
        left with p_left and to right 1-p_left

        input:
        ------
        N(int): Number of steps
        x_0(int): initial position
        p_left(float): probability to take a step left

        return:
        -------
        array(N): random walk series
        """
        steps = [x_0] + [ 1 if (i>p_left) else -1 for i in np.random.random(N-1)]
        return np.add.accumulate(steps)

    ##########
    # Fourier series 
    ##########
    def periodic_generator(coeffs: list, x):
        """generates a fourier series for given coefficient
        input:
        ======
        coeffs(list): list of coefficient
        x(N): np array
        return:
        =======
        y(N): np array
        """
        y = np.zeros(x.shape[0])
        num_terms = len(coeffs)
        for i in range(num_terms):
            y += coeffs[i]*np.sin(i*x)
        return y

    ##########
    # random coefficient generator
    ##########
    def coeff_generator(N:int):
        """generate a list of random numbers
        N: length of list
        """
        return np.random.rand(N).tolist()
    
    ##########
    # trend generator
    ##########
    def trend_generator(coeffs: np.array, x: np.array):
        """generates a trend for given coefficient for polynomial terms
        input:
        ======
        coeffs(np.array): list of polynomial coeeficient
        x(N): np array
        return:
        =======
        y(N): np array
        """
        i = 1
        y = np.zeros(x.shape[0])
        for l in coeffs:
            y += l * x**i
            i +=1
        return y
