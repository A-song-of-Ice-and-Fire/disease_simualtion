from disease_viz import run     
from utilities import ToolBox
if __name__ == "__main__":
    space_params = {
    "size_by_grid" : (1000,1000),         #400
    "size_by_pixel" : (100,100)
    }

    getBeta = ToolBox.getBetaFunction(0.4,1)      #基础感染概率为0.5，阈值距离为2
    
    population_params = {
        "individual_nums" : {
            "audience" : (200,200,200),
            "worker" : 1800,     #700
            "person" : 1200      #300
            },          #观赛者 工作者 普通人
        "init_I_nums" : {
            "audience" : (1,1,1),
            "worker" : 0,
            "person" : 0
        } ,
        "avg_end_distance" : 140
    }

    disease_params = {
        "infect_scope" : 3,
        "getBeta" : getBeta,
        "min_contact_distance" : 0
    }

    log_params = {
        "log_dir" : "./log" , 
        "step_in_record" : 5040
    }
    
    load_port = 8521
    run(space_params,population_params,disease_params,log_params,is_viz=False,seed=0,load_port=load_port)
