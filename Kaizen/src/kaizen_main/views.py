from django.shortcuts import render

# Create your views here.
def part1(request):
    return render(request,'kaizen_main/part1.html')


def part2(request):
    return render(request,'kaizen_main/part2.html')