from django.shortcuts import render
from . import translate

# Create your views here.
def translator_view(request):
  if request.method == 'POST':
    print("YEESSSSSS")
    original_text = request.POST['my_textarea']
    print(original_text)
    output = translate.translate(original_text)
    print(output)
   
    return render(request, 'translator.html', {'output_text': output, 'original_text': original_text})
  else:
    print('NOO')
    return render(request, 'translator.html')