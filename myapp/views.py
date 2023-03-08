from .predict import predict
from django.shortcuts import render


def upload_image(request):
    if request.method == 'POST':
        img = request.FILES['image']
        with open('image.jpg', 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        return render(request, 'result.html', {'image': 'image.jpg'})
    return render(request, 'upload.html')


def predict_image(request):
    if request.method == 'POST':
        image_path = request.POST['image_path']
        preds = predict(image_path)
        return render(request, 'result.html', {'preds': preds})
    return render(request, 'upload.html')
