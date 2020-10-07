.class public Lcom/daystrom/fbattery/EditPreferences;
.super Landroid/preference/PreferenceActivity;
.source "EditPreferences.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 6
    invoke-direct {p0}, Landroid/preference/PreferenceActivity;-><init>()V

    return-void
.end method


# virtual methods
.method public onCreate(Landroid/os/Bundle;)V
    .locals 1
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 9
    invoke-super {p0, p1}, Landroid/preference/PreferenceActivity;->onCreate(Landroid/os/Bundle;)V

    .line 10
    const/high16 v0, 0x7f040000

    invoke-virtual {p0, v0}, Lcom/daystrom/fbattery/EditPreferences;->addPreferencesFromResource(I)V

    .line 11
    return-void
.end method
