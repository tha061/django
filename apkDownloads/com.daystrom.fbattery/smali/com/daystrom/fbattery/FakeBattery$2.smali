.class Lcom/daystrom/fbattery/FakeBattery$2;
.super Ljava/lang/Object;
.source "FakeBattery.java"

# interfaces
.implements Landroid/content/DialogInterface$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/daystrom/fbattery/FakeBattery;->showException(Ljava/lang/Exception;)V
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
    iput-object p1, p0, Lcom/daystrom/fbattery/FakeBattery$2;->this$0:Lcom/daystrom/fbattery/FakeBattery;

    .line 249
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/content/DialogInterface;I)V
    .locals 0
    .param p1, "dialog"    # Landroid/content/DialogInterface;
    .param p2, "which"    # I

    .prologue
    .line 251
    invoke-interface {p1}, Landroid/content/DialogInterface;->cancel()V

    .line 252
    return-void
.end method
