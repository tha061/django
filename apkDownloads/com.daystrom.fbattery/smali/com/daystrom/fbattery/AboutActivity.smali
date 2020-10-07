.class public Lcom/daystrom/fbattery/AboutActivity;
.super Landroid/app/Activity;
.source "AboutActivity.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 8
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .locals 2
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 13
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 14
    const/high16 v1, 0x7f030000

    invoke-virtual {p0, v1}, Lcom/daystrom/fbattery/AboutActivity;->setContentView(I)V

    .line 17
    const v1, 0x7f08000b

    invoke-virtual {p0, v1}, Lcom/daystrom/fbattery/AboutActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    .line 18
    .local v0, "btnOk":Landroid/widget/Button;
    new-instance v1, Lcom/daystrom/fbattery/AboutActivity$1;

    invoke-direct {v1, p0}, Lcom/daystrom/fbattery/AboutActivity$1;-><init>(Lcom/daystrom/fbattery/AboutActivity;)V

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 24
    return-void
.end method
