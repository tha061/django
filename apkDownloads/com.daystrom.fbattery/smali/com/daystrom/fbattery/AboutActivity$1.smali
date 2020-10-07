.class Lcom/daystrom/fbattery/AboutActivity$1;
.super Ljava/lang/Object;
.source "AboutActivity.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/daystrom/fbattery/AboutActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/daystrom/fbattery/AboutActivity;


# direct methods
.method constructor <init>(Lcom/daystrom/fbattery/AboutActivity;)V
    .locals 0

    .prologue
    .line 1
    iput-object p1, p0, Lcom/daystrom/fbattery/AboutActivity$1;->this$0:Lcom/daystrom/fbattery/AboutActivity;

    .line 18
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1
    .param p1, "v"    # Landroid/view/View;

    .prologue
    .line 20
    iget-object v0, p0, Lcom/daystrom/fbattery/AboutActivity$1;->this$0:Lcom/daystrom/fbattery/AboutActivity;

    invoke-virtual {v0}, Lcom/daystrom/fbattery/AboutActivity;->finish()V

    .line 21
    return-void
.end method
