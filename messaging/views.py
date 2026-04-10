from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import PrivateMessage
from .forms import PrivateMessageForm


@login_required
def inbox(request):
    received_messages = PrivateMessage.objects.filter(
        receiver=request.user
    ).order_by("-created_at")

    return render(
        request,
        "messaging/inbox.html",
        {"received_messages": received_messages},
    )


@login_required
def send_message(request):
    if request.method == "POST":
        form = PrivateMessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect("messaging:inbox")
    else:
        form = PrivateMessageForm(user=request.user)

    return render(request, "messaging/send_message.html", {"form": form})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(PrivateMessage, pk=pk)

    if request.user != message.sender and request.user != message.receiver:
        return redirect("messaging:inbox")

    return render(request, "messaging/message_detail.html", {"message": message})