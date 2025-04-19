# Merge Model Predictions:

from sortedcontainers import SortedList
def get_top_predictions(predictions, N=2):
    response = {}

    for pred in predictions:
        if not pred['id'] in response.keys():
            response[pred['id']] = SortedList(key=lambda x: -x[1])
        
        response[pred['id']].add((pred['model'],pred['score']))
    
    # return top-K
    for key in response.keys():
        response[key] = list(response[key])[:N]

    return response


if __name__=='__main__':
    predictions = [
    {"id": "user1", "model": "bert_v1", "score": 0.91},
    {"id": "user1", "model": "xgboost_v2", "score": 0.88},
    {"id": "user1", "model": "bert_v2", "score": 0.96},
    {"id": "user2", "model": "bert_v2", "score": 0.82},
    {"id": "user2", "model": "xgboost_v2", "score": 0.84},
    ]
    print(get_top_predictions(predictions,1))