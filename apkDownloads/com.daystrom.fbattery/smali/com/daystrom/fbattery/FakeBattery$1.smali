.class Lcom/daystrom/fbattery/FakeBattery$1;
.super Ljava/lang/Object;
.source "FakeBattery.java"

# interfaces
.implements Landroid/view/View$OnLongClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/daystrom/fbattery/FakeBattery;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/daystrom/fbattery/FakeBattery;


# direct methods
.method constructor <init>(Lcom/daystrom/fbattery/FakeBattery;)V
    .locals 0

    .prologue
    .line 1
    iput-object p1, p0, Lcom/daystrom/fbattery/FakeBattery$1;->this$0:Lcom/daystrom/fbattery/FakeBattery;

    .line 93
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onLongClick(Landroid/view/View;)Z
    .locals 1
    .param p1, "v"    # Landroid/view/View;

    .prologue
    .line 95
    iget-object v0, p0, Lcom/daystrom/fbattery/FakeBattery$1;->this$0:Lcom/daystrom/fbattery/FakeBattery;

    invoke-virtual {v0}, Lcom/daystrom/fbattery/FakeBattery;->finish()V

    .line 96
    const/4 v0, 0x1

    return v0
.end method
