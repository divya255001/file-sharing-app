from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def dashboard(request):
    files = UploadedFile.objects.filter(user=request.user)
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('dashboard')
    else:
        form = FileUploadForm()
    return render(request,'dashboard.html', {'form': form, 'files': files})
@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id, user=request.user)
    if request.method == 'POST':
        file.delete()
        messages.success(request, 'File deleted successfully.')
    return redirect('dashboard')
