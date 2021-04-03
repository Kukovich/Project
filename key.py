objects = [{
    "math": [
    {  
        "1": [
        {
            "variants_of_task": [
            {
                "difficult": "1",
                "question": "текст задания",
                "answer": "ответ"
            }, 
            {
                "difficult": "2",
                "question": "текст задания",
                "answer": "ответ"
            },
            {
                "difficult": "3",
                "question": "текст задания",
                "answer": "ответ"
            }]
        }]
    },
    {
        "2": [
        {
            "variants_of_task": [
            {
                "difficult": "1",
                "question": "текст задания",
                "answer": "ответ"
            }, 
            {
                "difficult": "2",
                "question": "текст задания",
                "answer": "ответ"
            },
            {
                "difficult": "3",
                "question": "текст задания",
                "answer": "ответ"
            }]
        }]
    },
    {
       "3": [
        {
            "variants_of_task": [
            {
                "difficult": "1",
                "question": "текст задания",
                "answer": "ответ"
            }, 
            {
                "difficult": "2",
                "question": "текст задания",
                "answer": "ответ"
            },
            {
                "difficult": "3",
                "question": "текст задания",
                "answer": "ответ"
            }]
        }] 
    }]
},
{
    "rus": [
    {  
        "1": [
        {
            "variants_of_task": [
            {
                "difficult": "1",
                "question": "текст задания",
                "answer": "ответ"
            }, 
            {
                "difficult": "2",
                "question": "текст задания",
                "answer": "ответ"
            },
            {
                "difficult": "3",
                "question": "текст задания",
                "answer": "ответ"
            }]
        }]
    },
    {
        "2": [
        {
            "variants_of_task": [
            {
                "difficult": "1",
                "question": "текст задания",
                "answer": "ответ"
            }, 
            {
                "difficult": "2",
                "question": "текст задания",
                "answer": "ответ"
            },
            {
                "difficult": "3",
                "question": "текст задания",
                "answer": "ответ"
            }]
        }]
    },
    {
       "3": [
        {
            "variants_of_task": [
            {
                "difficult": "1",
                "question": "текст задания",
                "answer": "ответ"
            }, 
            {
                "difficult": "2",
                "question": "текст задания",
                "answer": "ответ"
            },
            {
                "difficult": "3",
                "question": "текст задания",
                "answer": "ответ"
            }]
        }] 
    }]
}]

print(objects[1]["rus"][2]["3"][0]["variants_of_task"][1]["answer"])