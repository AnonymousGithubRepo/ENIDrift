from numpy import *
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class SubLearn():
    
    def __init__(self, learner='PCA', num_simulation=100, time_test=100,
                 ensemble_size=100, alpha=0.05):
        
        self.learner = learner
        self.num_simulation = num_simulation
        self.ensemble_size = ensemble_size
        self.time_test = time_test
        self.learner_pool = []
        self.threshold_list = []
        self.alpha = alpha
        self.scaler_pool = []
    
    def train(self, t):
        
        model = PCA(n_components=0.99)
        model.fit(t)
        scores = model.score_samples(t)
        self.threshold_list = sorted(scores)[0]
        self.learner_pool = model
        """
        x = mat(x)
        all_idx = arange(x.shape[0])
        k = int(sqrt(x.shape[0]))
        
        for i in range(self.num_simulation):
            
            t_idx = all_idx
            random.shuffle(t_idx)
            
            # if self.replace == True:
            # if self.replace == False:
            sampled_data = x[t_idx[:k]]
            
            # scaler = StandardScaler()
            # sampled_data = scaler.fit_transform(sampled_data)
            # self.scaler_pool.append(scaler)
            
            # if self.l == 'PCA':
            model = PCA(n_components=0.99)
            model.fit(sampled_data)
            
            try:
                scores = model.score_samples(sampled_data)
            except:
                print(sampled_data)
                print(sampled_data.shape)
                print(str(isinf(sampled_data).any == True))
                print(str(isnan(sampled_data).any == True))
                print(str(x.shape))
                scores = model.score_samples(sampled_data)
            
            self.threshold_list.append(sorted(scores)[int(k*self.alpha)])
            self.learner_pool.append(model)
        """
    
    def pred(self, x):
        
        result = [0]*x.shape[0]
        
        for i in range(x.shape[0]):
            if self.threshold_list <= self.learner_pool.score(x[i].reshape(1, -1)):
                result[i] = 1
        
        """
        temp_result = zeros((self.time_test, self.ensemble_size))
        all_pred = zeros((self.num_simulation, ))
        for i in range(self.num_simulation):
            if self.threshold_list[i] <= self.learner_pool[i].score(x.reshape(1, -1)):
                all_pred[i] = 1 # belong to the class
            else:
                all_pred[i] = 0 # doesn't belong to the class
        
        for i in range(self.time_test):
            rand_idx = random.permutation(self.num_simulation)
            temp_result[i, :] = all_pred[rand_idx[:self.ensemble_size]]
        
        pred_result = mean(temp_result, 1)
        """
        return result