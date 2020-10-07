.class public Lcom/daystrom/fbattery/FakeBattery;
.super Landroid/app/Activity;
.source "FakeBattery.java"


# static fields
.field private static final ANDROID_1X_LAST_VERSION:I = 0x4

.field private static final APPLICATION_VERSION:Ljava/lang/String; = "APPLICATION_VERSION"

.field private static final BATTERY_TYPE_ANDROID:Ljava/lang/String; = "ANDROID"

.field private static final BATTERY_TYPE_HTC_WIDGET:Ljava/lang/String; = "HTC_WIDGET"

.field private static final HOME_ANDROID_1X:Ljava/lang/String; = "ANDROID_1X"

.field private static final HOME_ANDROID_2_1:Ljava/lang/String; = "ANDROID_2_1"

.field private static final HOME_ANDROID_2_2:Ljava/lang/String; = "ANDROID_2_2"

.field private static final HOME_ANDROID_2_3:Ljava/lang/String; = "ANDROID_2_3"

.field private static final HOME_HTC_SENSE:Ljava/lang/String; = "HTC_SENSE"

.field private static final LIST_BATTERY_PREFERENCES:Ljava/lang/String; = "list_battery_preference_key"

.field private static final LIST_HOME_PREFERENCES:Ljava/lang/String; = "list_home_preference_key"

.field private static final LIST_NOTIFICATION_PREFERENCES:Ljava/lang/String; = "list_notification_preference_key"

.field private static final MENU_ABOUT:I = 0x4

.field private static final MENU_EXIT:I = 0x1

.field private static final MENU_SCREENSHOT:I = 0x2

.field private static final MENU_SETTINGS:I = 0x3

.field private static final NOTIFICATION_TYPE_ANDROID:Ljava/lang/String; = "ANDROID"

.field private static final NOTIFICATION_TYPE_ANDROID_2_3:Ljava/lang/String; = "ANDROID_2_3"

.field private static final NOTIFICATION_TYPE_HTC_SENSE:Ljava/lang/String; = "HTC_SENSE"


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 23
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    return-void
.end method

.method private showException(Ljava/lang/Exception;)V
    .locals 4
    .param p1, "e"    # Ljava/lang/Exception;

    .prologue
    .line 248
    new-instance v0, Landroid/app/AlertDialog$Builder;

    invoke-direct {v0, p0}, Landroid/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    .line 249
    .local v0, "builder":Landroid/app/AlertDialog$Builder;
    new-instance v1, Ljava/lang/StringBuilder;

    const-string v2, "Fatal error: "

    invoke-direct {v1, v2}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V

    invoke-virtual {p1}, Ljava/lang/Exception;->getMessage()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setMessage(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    move-result-object v1

    const-string v2, "OK"

    new-instance v3, Lcom/daystrom/fbattery/FakeBattery$2;

    invoke-direct {v3, p0}, Lcom/daystrom/fbattery/FakeBattery$2;-><init>(Lcom/daystrom/fbattery/FakeBattery;)V

    invoke-virtual {v1, v2, v3}, Landroid/app/AlertDialog$Builder;->setPositiveButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder;

    .line 254
    invoke-virtual {v0}, Landroid/app/AlertDialog$Builder;->show()Landroid/app/AlertDialog;

    .line 255
    return-void
.end method


# virtual methods
.method public getPreferences()V
    .locals 25

    .prologue
    .line 121
    invoke-virtual/range {p0 .. p0}, Lcom/daystrom/fbattery/FakeBattery;->getResources()Landroid/content/res/Resources;

    move-result-object v22

    const v23, 0x7f050001

    invoke-virtual/range {v22 .. v23}, Landroid/content/res/Resources;->getColor(I)I

    move-result v8

    .line 122
    .local v8, "color_white":I
    invoke-virtual/range {p0 .. p0}, Lcom/daystrom/fbattery/FakeBattery;->getResources()Landroid/content/res/Resources;

    move-result-object v22

    const/high16 v23, 0x7f050000

    invoke-virtual/range {v22 .. v23}, Landroid/content/res/Resources;->getColor(I)I

    move-result v7

    .line 125
    .local v7, "color_black":I
    invoke-static/range {p0 .. p0}, Landroid/preference/PreferenceManager;->getDefaultSharedPreferences(Landroid/content/Context;)Landroid/content/SharedPreferences;

    move-result-object v9

    .line 128
    .local v9, "fbatteryPrefs":Landroid/content/SharedPreferences;
    const-string v22, "APPLICATION_VERSION"

    const-string v23, ""

    move-object v0, v9

    move-object/from16 v1, v22

    move-object/from16 v2, v23

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v21

    .line 129
    .local v21, "versionPreference":Ljava/lang/String;
    const v22, 0x7f070002

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v4

    .line 132
    .local v4, "applicationVersion":Ljava/lang/String;
    move-object/from16 v0, v21

    move-object v1, v4

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-nez v22, :cond_0

    .line 133
    invoke-interface {v9}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;

    move-result-object v10

    .line 134
    .local v10, "fbatteryPrefsEditor":Landroid/content/SharedPreferences$Editor;
    const-string v22, "APPLICATION_VERSION"

    move-object v0, v10

    move-object/from16 v1, v22

    move-object v2, v4

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;

    .line 135
    invoke-interface {v10}, Landroid/content/SharedPreferences$Editor;->commit()Z

    .line 139
    .end local v10    # "fbatteryPrefsEditor":Landroid/content/SharedPreferences$Editor;
    :cond_0
    const-string v22, ""

    invoke-virtual/range {v21 .. v22}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_1

    .line 142
    const v22, 0x7f070003

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v19

    .line 143
    .local v19, "text":Ljava/lang/CharSequence;
    invoke-virtual/range {p0 .. p0}, Lcom/daystrom/fbattery/FakeBattery;->getApplicationContext()Landroid/content/Context;

    move-result-object v22

    const/16 v23, 0x1

    move-object/from16 v0, v22

    move-object/from16 v1, v19

    move/from16 v2, v23

    invoke-static {v0, v1, v2}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v20

    .line 144
    .local v20, "toast":Landroid/widget/Toast;
    const/16 v22, 0x10

    const/16 v23, 0x0

    const/16 v24, 0x0

    move-object/from16 v0, v20

    move/from16 v1, v22

    move/from16 v2, v23

    move/from16 v3, v24

    invoke-virtual {v0, v1, v2, v3}, Landroid/widget/Toast;->setGravity(III)V

    .line 145
    invoke-virtual/range {v20 .. v20}, Landroid/widget/Toast;->show()V

    .line 148
    new-instance v22, Landroid/content/Intent;

    const-class v23, Lcom/daystrom/fbattery/EditPreferences;

    move-object/from16 v0, v22

    move-object/from16 v1, p0

    move-object/from16 v2, v23

    invoke-direct {v0, v1, v2}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    move-object/from16 v0, p0

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->startActivity(Landroid/content/Intent;)V

    .line 152
    .end local v19    # "text":Ljava/lang/CharSequence;
    .end local v20    # "toast":Landroid/widget/Toast;
    :cond_1
    const-string v22, "list_notification_preference_key"

    const-string v23, "ANDROID"

    move-object v0, v9

    move-object/from16 v1, v22

    move-object/from16 v2, v23

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v15

    .line 153
    .local v15, "notificationPreference":Ljava/lang/String;
    const v22, 0x7f08000e

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v18

    check-cast v18, Landroid/widget/TableLayout;

    .line 154
    .local v18, "objTableLayoutStatusBar":Landroid/widget/TableLayout;
    const v22, 0x7f080012

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v16

    check-cast v16, Landroid/widget/DigitalClock;

    .line 156
    .local v16, "objDigitalClock":Landroid/widget/DigitalClock;
    const-string v22, "ANDROID"

    move-object v0, v15

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_2

    .line 157
    const v22, 0x7f020008

    move-object/from16 v0, v18

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/TableLayout;->setBackgroundResource(I)V

    .line 158
    move-object/from16 v0, v16

    move v1, v7

    invoke-virtual {v0, v1}, Landroid/widget/DigitalClock;->setTextColor(I)V

    .line 175
    :goto_0
    const v22, 0x7f08000f

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v12

    check-cast v12, Landroid/widget/ImageView;

    .line 176
    .local v12, "imageView3g":Landroid/widget/ImageView;
    const v22, 0x7f080010

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v14

    check-cast v14, Landroid/widget/ImageView;

    .line 177
    .local v14, "imageViewSignal":Landroid/widget/ImageView;
    const v22, 0x7f080011

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v13

    check-cast v13, Landroid/widget/ImageView;

    .line 179
    .local v13, "imageViewBattery":Landroid/widget/ImageView;
    const-string v22, "ANDROID"

    move-object v0, v15

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_5

    .line 180
    const v22, 0x7f02000d

    move-object v0, v12

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 181
    const v22, 0x7f020010

    move-object v0, v14

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 182
    const v22, 0x7f02000b

    move-object v0, v13

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 202
    :goto_1
    const-string v22, "list_battery_preference_key"

    const-string v23, "ANDROID"

    move-object v0, v9

    move-object/from16 v1, v22

    move-object/from16 v2, v23

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    .line 203
    .local v5, "batteryPreference":Ljava/lang/String;
    const v22, 0x7f080016

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v6

    check-cast v6, Landroid/widget/ImageView;

    .line 205
    .local v6, "btnImageViewClickable":Landroid/widget/ImageView;
    const-string v22, "ANDROID"

    move-object v0, v5

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_8

    .line 206
    const v22, 0x7f020006

    move-object v0, v6

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 217
    :goto_2
    const-string v22, "list_home_preference_key"

    const-string v23, "ANDROID_1X"

    move-object v0, v9

    move-object/from16 v1, v22

    move-object/from16 v2, v23

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v11

    .line 218
    .local v11, "homePreference":Ljava/lang/String;
    const v22, 0x7f080014

    move-object/from16 v0, p0

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v17

    check-cast v17, Landroid/widget/ImageView;

    .line 220
    .local v17, "objImageViewHome":Landroid/widget/ImageView;
    const-string v22, "ANDROID_1X"

    move-object v0, v11

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_a

    .line 221
    const/high16 v22, 0x7f020000

    move-object/from16 v0, v17

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 240
    :goto_3
    return-void

    .line 160
    .end local v5    # "batteryPreference":Ljava/lang/String;
    .end local v6    # "btnImageViewClickable":Landroid/widget/ImageView;
    .end local v11    # "homePreference":Ljava/lang/String;
    .end local v12    # "imageView3g":Landroid/widget/ImageView;
    .end local v13    # "imageViewBattery":Landroid/widget/ImageView;
    .end local v14    # "imageViewSignal":Landroid/widget/ImageView;
    .end local v17    # "objImageViewHome":Landroid/widget/ImageView;
    :cond_2
    const-string v22, "ANDROID_2_3"

    move-object v0, v15

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_3

    .line 161
    const v22, 0x7f020009

    move-object/from16 v0, v18

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/TableLayout;->setBackgroundResource(I)V

    .line 162
    move-object/from16 v0, v16

    move v1, v8

    invoke-virtual {v0, v1}, Landroid/widget/DigitalClock;->setTextColor(I)V

    goto/16 :goto_0

    .line 164
    :cond_3
    const-string v22, "HTC_SENSE"

    move-object v0, v15

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_4

    .line 165
    const v22, 0x7f02000a

    move-object/from16 v0, v18

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/TableLayout;->setBackgroundResource(I)V

    .line 166
    move-object/from16 v0, v16

    move v1, v8

    invoke-virtual {v0, v1}, Landroid/widget/DigitalClock;->setTextColor(I)V

    goto/16 :goto_0

    .line 170
    :cond_4
    const v22, 0x7f020008

    move-object/from16 v0, v18

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/TableLayout;->setBackgroundResource(I)V

    .line 171
    move-object/from16 v0, v16

    move v1, v7

    invoke-virtual {v0, v1}, Landroid/widget/DigitalClock;->setTextColor(I)V

    goto/16 :goto_0

    .line 184
    .restart local v12    # "imageView3g":Landroid/widget/ImageView;
    .restart local v13    # "imageViewBattery":Landroid/widget/ImageView;
    .restart local v14    # "imageViewSignal":Landroid/widget/ImageView;
    :cond_5
    const-string v22, "ANDROID_2_3"

    move-object v0, v15

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_6

    .line 185
    const v22, 0x7f02000f

    move-object v0, v12

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 186
    const v22, 0x7f020011

    move-object v0, v14

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 187
    const v22, 0x7f02000c

    move-object v0, v13

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_1

    .line 189
    :cond_6
    const-string v22, "HTC_SENSE"

    move-object v0, v15

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_7

    .line 190
    const v22, 0x7f02000e

    move-object v0, v12

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 191
    const v22, 0x7f020012

    move-object v0, v14

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 192
    const v22, 0x7f02000b

    move-object v0, v13

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_1

    .line 196
    :cond_7
    const v22, 0x7f02000d

    move-object v0, v12

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 197
    const v22, 0x7f020010

    move-object v0, v14

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 198
    const v22, 0x7f02000b

    move-object v0, v13

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_1

    .line 208
    .restart local v5    # "batteryPreference":Ljava/lang/String;
    .restart local v6    # "btnImageViewClickable":Landroid/widget/ImageView;
    :cond_8
    const-string v22, "HTC_WIDGET"

    move-object v0, v5

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_9

    .line 209
    const v22, 0x7f020007

    move-object v0, v6

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_2

    .line 213
    :cond_9
    const v22, 0x7f020006

    move-object v0, v6

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_2

    .line 223
    .restart local v11    # "homePreference":Ljava/lang/String;
    .restart local v17    # "objImageViewHome":Landroid/widget/ImageView;
    :cond_a
    const-string v22, "ANDROID_2_1"

    move-object v0, v11

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_b

    .line 224
    const v22, 0x7f020001

    move-object/from16 v0, v17

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_3

    .line 226
    :cond_b
    const-string v22, "ANDROID_2_2"

    move-object v0, v11

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_c

    .line 227
    const v22, 0x7f020002

    move-object/from16 v0, v17

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_3

    .line 229
    :cond_c
    const-string v22, "ANDROID_2_3"

    move-object v0, v11

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_d

    .line 230
    const v22, 0x7f020003

    move-object/from16 v0, v17

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_3

    .line 232
    :cond_d
    const-string v22, "HTC_SENSE"

    move-object v0, v11

    move-object/from16 v1, v22

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v22

    if-eqz v22, :cond_e

    .line 233
    const v22, 0x7f020004

    move-object/from16 v0, v17

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_3

    .line 237
    :cond_e
    const/high16 v22, 0x7f020000

    move-object/from16 v0, v17

    move/from16 v1, v22

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setImageResource(I)V

    goto/16 :goto_3
.end method

.method public onCreate(Landroid/os/Bundle;)V
    .locals 8
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 60
    :try_start_0
    sget v3, Landroid/os/Build$VERSION;->SDK_INT:I

    .line 61
    .local v3, "osVersion":I
    const/4 v6, 0x4

    if-gt v3, v6, :cond_2

    const/4 v6, 0x1

    move v4, v6

    .line 64
    .local v4, "osVersion1x":Z
    :goto_0
    if-eqz v4, :cond_3

    .line 66
    const v6, 0x1030007

    invoke-virtual {p0, v6}, Lcom/daystrom/fbattery/FakeBattery;->setTheme(I)V

    .line 73
    :goto_1
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 74
    const v6, 0x7f030001

    invoke-virtual {p0, v6}, Lcom/daystrom/fbattery/FakeBattery;->setContentView(I)V

    .line 77
    if-eqz v4, :cond_0

    .line 78
    const v6, 0x7f08000d

    invoke-virtual {p0, v6}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Landroid/widget/LinearLayout;

    .line 79
    .local v2, "objLinearLayoutMain":Landroid/widget/LinearLayout;
    invoke-virtual {p0}, Lcom/daystrom/fbattery/FakeBattery;->getApplicationContext()Landroid/content/Context;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/Context;->getWallpaper()Landroid/graphics/drawable/Drawable;

    move-result-object v5

    check-cast v5, Landroid/graphics/drawable/BitmapDrawable;

    .line 80
    .local v5, "wallpaperDrawable":Landroid/graphics/drawable/BitmapDrawable;
    new-instance v6, Lcom/daystrom/fbattery/FastBitmapDrawable;

    invoke-virtual {v5}, Landroid/graphics/drawable/BitmapDrawable;->getBitmap()Landroid/graphics/Bitmap;

    move-result-object v7

    invoke-direct {v6, v7}, Lcom/daystrom/fbattery/FastBitmapDrawable;-><init>(Landroid/graphics/Bitmap;)V

    invoke-virtual {v2, v6}, Landroid/widget/LinearLayout;->setBackgroundDrawable(Landroid/graphics/drawable/Drawable;)V

    .line 84
    .end local v2    # "objLinearLayoutMain":Landroid/widget/LinearLayout;
    .end local v5    # "wallpaperDrawable":Landroid/graphics/drawable/BitmapDrawable;
    :cond_0
    const v6, 0x7f080016

    invoke-virtual {p0, v6}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    .line 92
    .local v0, "btnImageViewClickable":Landroid/widget/ImageView;
    if-eqz v0, :cond_1

    .line 93
    new-instance v6, Lcom/daystrom/fbattery/FakeBattery$1;

    invoke-direct {v6, p0}, Lcom/daystrom/fbattery/FakeBattery$1;-><init>(Lcom/daystrom/fbattery/FakeBattery;)V

    invoke-virtual {v0, v6}, Landroid/widget/ImageView;->setOnLongClickListener(Landroid/view/View$OnLongClickListener;)V

    .line 104
    .end local v0    # "btnImageViewClickable":Landroid/widget/ImageView;
    .end local v3    # "osVersion":I
    .end local v4    # "osVersion1x":Z
    :cond_1
    :goto_2
    return-void

    .line 61
    .restart local v3    # "osVersion":I
    :cond_2
    const/4 v6, 0x0

    move v4, v6

    goto :goto_0

    .line 70
    .restart local v4    # "osVersion1x":Z
    :cond_3
    const v6, 0x1030060

    invoke-virtual {p0, v6}, Lcom/daystrom/fbattery/FakeBattery;->setTheme(I)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1

    .line 101
    .end local v3    # "osVersion":I
    .end local v4    # "osVersion1x":Z
    :catch_0
    move-exception v6

    move-object v1, v6

    .line 102
    .local v1, "e":Ljava/lang/Exception;
    invoke-direct {p0, v1}, Lcom/daystrom/fbattery/FakeBattery;->showException(Ljava/lang/Exception;)V

    goto :goto_2
.end method

.method public onCreateOptionsMenu(Landroid/view/Menu;)Z
    .locals 4
    .param p1, "menu"    # Landroid/view/Menu;

    .prologue
    const/4 v3, 0x1

    const/4 v2, 0x0

    .line 262
    const v0, 0x7f070006

    invoke-virtual {p0, v0}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-interface {p1, v2, v3, v2, v0}, Landroid/view/Menu;->add(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;

    move-result-object v0

    const v1, 0x1080038

    invoke-interface {v0, v1}, Landroid/view/MenuItem;->setIcon(I)Landroid/view/MenuItem;

    .line 263
    const/4 v0, 0x2

    const v1, 0x7f070007

    invoke-virtual {p0, v1}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-interface {p1, v2, v0, v2, v1}, Landroid/view/Menu;->add(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;

    move-result-object v0

    const v1, 0x1080037

    invoke-interface {v0, v1}, Landroid/view/MenuItem;->setIcon(I)Landroid/view/MenuItem;

    .line 264
    const/4 v0, 0x3

    const v1, 0x7f070008

    invoke-virtual {p0, v1}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-interface {p1, v2, v0, v2, v1}, Landroid/view/Menu;->add(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;

    move-result-object v0

    const v1, 0x1080049

    invoke-interface {v0, v1}, Landroid/view/MenuItem;->setIcon(I)Landroid/view/MenuItem;

    .line 265
    const/4 v0, 0x4

    const v1, 0x7f070009

    invoke-virtual {p0, v1}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-interface {p1, v2, v0, v2, v1}, Landroid/view/Menu;->add(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;

    move-result-object v0

    const v1, 0x1080041

    invoke-interface {v0, v1}, Landroid/view/MenuItem;->setIcon(I)Landroid/view/MenuItem;

    .line 266
    return v3
.end method

.method public onOptionsItemSelected(Landroid/view/MenuItem;)Z
    .locals 6
    .param p1, "item"    # Landroid/view/MenuItem;

    .prologue
    const/4 v5, 0x1

    .line 274
    invoke-interface {p1}, Landroid/view/MenuItem;->getItemId()I

    move-result v3

    packed-switch v3, :pswitch_data_0

    .line 291
    const/4 v3, 0x0

    :goto_0
    return v3

    .line 276
    :pswitch_0
    invoke-virtual {p0}, Lcom/daystrom/fbattery/FakeBattery;->finish()V

    move v3, v5

    .line 277
    goto :goto_0

    .line 279
    :pswitch_1
    invoke-virtual {p0}, Lcom/daystrom/fbattery/FakeBattery;->getApplicationContext()Landroid/content/Context;

    move-result-object v1

    .line 280
    .local v1, "context":Landroid/content/Context;
    const v3, 0x7f08000d

    invoke-virtual {p0, v3}, Lcom/daystrom/fbattery/FakeBattery;->findViewById(I)Landroid/view/View;

    move-result-object v2

    check-cast v2, Landroid/widget/LinearLayout;

    .line 281
    .local v2, "view":Landroid/view/View;
    const/high16 v3, 0x7f070000

    invoke-virtual {p0, v3}, Lcom/daystrom/fbattery/FakeBattery;->getString(I)Ljava/lang/String;

    move-result-object v0

    .line 282
    .local v0, "appName":Ljava/lang/String;
    invoke-virtual {v2}, Landroid/view/View;->getRootView()Landroid/view/View;

    move-result-object v3

    invoke-static {v1, v3, v0}, Lcom/daystrom/fbattery/ScreenShot;->shot(Landroid/content/Context;Landroid/view/View;Ljava/lang/String;)V

    move v3, v5

    .line 283
    goto :goto_0

    .line 285
    .end local v0    # "appName":Ljava/lang/String;
    .end local v1    # "context":Landroid/content/Context;
    .end local v2    # "view":Landroid/view/View;
    :pswitch_2
    new-instance v3, Landroid/content/Intent;

    const-class v4, Lcom/daystrom/fbattery/EditPreferences;

    invoke-direct {v3, p0, v4}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    invoke-virtual {p0, v3}, Lcom/daystrom/fbattery/FakeBattery;->startActivity(Landroid/content/Intent;)V

    move v3, v5

    .line 286
    goto :goto_0

    .line 288
    :pswitch_3
    new-instance v3, Landroid/content/Intent;

    const-class v4, Lcom/daystrom/fbattery/AboutActivity;

    invoke-direct {v3, p0, v4}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    invoke-virtual {p0, v3}, Lcom/daystrom/fbattery/FakeBattery;->startActivity(Landroid/content/Intent;)V

    move v3, v5

    .line 289
    goto :goto_0

    .line 274
    nop

    :pswitch_data_0
    .packed-switch 0x1
        :pswitch_0
        :pswitch_1
        :pswitch_2
        :pswitch_3
    .end packed-switch
.end method

.method public onResume()V
    .locals 0

    .prologue
    .line 108
    invoke-super {p0}, Landroid/app/Activity;->onResume()V

    .line 111
    invoke-virtual {p0}, Lcom/daystrom/fbattery/FakeBattery;->getPreferences()V

    .line 113
    return-void
.end method
