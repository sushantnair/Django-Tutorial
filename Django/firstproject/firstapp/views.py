from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
monthly_rewards = {
    "january": "Go for a picnic",
    "february": "Go to an anusement park",
    "march": "",
}
def monthly_reward(request, month):
    try:
        reward_text = monthly_rewards[month]
        response_data = render_to_string("firstapp/reward.html")
        # return HttpResponse(response_data)
        '''
        return render(request, "firstapp/reward2.html", {
            "text": reward_text
        })
        '''
        '''
        return render(request, "firstapp/reward3.html", {
            "text": reward_text, "month_name": month
        })
        '''
        
        return render(request, "firstapp/reward4.html", {
            "text": reward_text, "month_name": month
        })
        

    except:
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        return render(request, "404.html")
    
def monthly_reward_list(request):
    months = list(monthly_rewards.keys())
    '''
    return render(request, "firstapp/allrewards.html", {
        "months": months
    })
    '''
    '''
    return render(request, "firstapp/allrewardslinked.html", {
        "months": months
    })
    '''
    '''
    return render(request, "firstapp/allrewardslinkedalternate.html", {
        "months": months
    })
    '''
    '''
    return render(request, "firstapp/allrewardslinkedextended.html", {
        "months": months
    })
    '''
    '''
    return render(request, "firstapp/allrewardslinkedextendedstyled1A.html", {
        "months": months
    })
    '''
    '''
    return render(request, "firstapp/allrewardslinkedextendedstyled1B.html", {
        "months": months
    })
    '''
    '''
    return render(request, "firstapp/allrewardslinkedextendedstyled2A.html", {
        "months": months
    })
    '''
    
    return render(request, "firstapp/allrewardslinkedextendedstyled2B.html", {
        "months": months
    })
    
