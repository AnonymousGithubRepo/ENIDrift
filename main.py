import time
from iP2Vmain import *
from numpy import *
from pandas import *
from measure import *
from iP2Vmain import *

settings = {
        'data_name': 'CICIDS2017-Wednesday',
        'num_run': 1,
        'release_speed': 1000,
        'lamda': [0.1, 0.1],
        'delta': [0.05, 0.05],
        'incremental': True,
        'save': False,
        'vector': True
        }




days = ['0401', '0402', '0403', '0701', '0702', '0703', '0901', '0902', '0903']
lamda_list = [0.3, 0, 0.1, 0.2, 0.4, 0.5, 1, 2]




for la in lamda_list:
    for day in days:
        
        path_packet = '..//'+str(day)+'ExtractKeyField.csv'
        path_label = 'label//'+str(day)+'label.npy'
        
        vec = settings['vector']
        
        if vec:
            path_vector = 'iP2V//iP2Vextracttest'+str(day)+'.npy'
        else:
            path_vector = '-1'
        
        ############################################################################
        
        num_run = settings['num_run']
        release_speed = settings['release_speed']
        lamd = la
        delt = settings['delta']
        incre = settings['incremental']
        s = settings['save']
        label = load(path_label)
#        packets = read_csv(path_packet)
        
        if vec:
            vector_packet = load(path_vector)
        else:
            vector_packet = zeros((300000, 200))
        
        num_vec = vector_packet.shape[0]
        
        for i_run in range(num_run):
            ENIDrift = ENIDrifttrain(lamda = lamd, delta=delt, incremental=incre)
            #FE = iP2Vmain(path = path_packet, incremental=incre)
            
            ZAREF.loadpara()
            #FE.loadpara()
            
            prediction = []
            
            num_released = 0
            
            start = time.time()
            for i_packet in range(num_vec):
                
                if i_packet%50000 == 0:
                    print(str(i_packet)+' processed...')
                
                # Execute
                prediction.append(ENIDrift.predict(vector_packet[i_packet,:].reshape(1, -1)))
                
                # Release labels
                if i_packet % release_speed == 0:
                    ENIDrift.update(label[num_released:i_packet+1])
                    num_released = i_packet + 1
            
            stop = time.time()
#            if s:
#                ENIDrift.save()
#                if not vec:
#                    FE.save()
            print("Time elapsed for day "+str(day)+" lamda "+str(la)+": "+str(stop-start)+" seconds")
            
            # result: tp, fp, tn, fn, f1, gmean
            save(("result//"+str(day)+"predictionresult"+str(la)+".npy"), prediction)
            result = evaluate(prediction, label, (str(day)+str(la)))
            save(("result//"+str(day)+"resultNF"+str(la)+".npy"), result)
            overall(prediction, label, (str(day)+str(la)))