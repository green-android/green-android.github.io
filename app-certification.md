# 绿色应用认证计划

为推广和促进[《绿色应用公约》](app-convention.html)在国内Android应用生态中的普遍接纳，推动更多有责任感的开发团队积极加入改善Android设备体验的行列，[绿色守护（Greenify）](http://www.coolapk.com/apk/com.oasisfeng.greenify)联合国内主流的科技媒体、应用社区和传播渠道共同推出绿色应用认证计划，加大在普通用户群体中对设备体验的科普教育，并对遵守公约捍卫设备体验的优秀应用进行宣传推广，促进从用户、应用开发团队到设备厂商对公约所提倡的设备体验原则的普遍认同，弥合整个生态中日渐分裂的应用后台行为和限制约束。

通过认证的应用，将有机会获得在公约网站及相关媒体、宣传渠道的推广。 **在应用中添加『已通过《Android 绿色应用公约》认证』信息（通常在『关于』或『设置』界面中），并链接到公约官方网站的应用，将获得更靠前的推广位次。** （请在认证申请 issue 中附上截图）

# 认证要求

针对国内的复杂国情（尤其是推送渠道的碎片化问题），以维护应用的合理利益为出发点，在《绿色应用公约》的基础上，补充以下辅助内容：

1. 公约中的第1点要求仅约束应用在`AndroidManifest.xml`中声明的`targetSdkVersion`属性，对`minSdkVersion`属性和开发中使用的SDK版本无要求。开发团队须自行确保应用符合[Android系统本身对`targetSdkVersion`的约束要求](https://developer.android.google.cn/reference/android/os/Build.VERSION_CODES.html#N)。

2. 针对公约中的第2点要求，可能有部分三方SDK要求必须在`AndroidManifest.xml`中声明`READ_PHONE_STATE`权限，否则拒绝工作。 **解决方法是保留权限声明，但不在运行期请求此项权限。**

   经过与相关SDK开发团队的沟通，统计和Push类SDK其实并不依赖这一权限，因为一方面不含基带的Android设备（如大部分平板电脑）都没有IMEI，另一方面有部分国内厂商的Android系统中已主动屏蔽了对真实IMEI的读取，所以三方SDK的实现中都不会强依赖IMEI。（实际上读取IMEI大多也是服务于用户身份的跨应用关联，属于SDK提供团队的利益诉求）

3. 针对公约中的第3点要求，如果应用中集成了国内的第三方SDK，则需要评估其是否存在『交叉唤醒』行为（典型如国内的大部分推送SDK）。 **建议接入轻量的开源辅助库[Project Condom](https://github.com/oasisfeng/condom)，识别和消除第三方SDK造成的交叉唤醒。**

4. 针对公约中的第4点要求，请通过`dumpsys alarm`和`dumpsys jobscheduler <package name>`完成自查。

5. 针对公约中的第5点要求，如果应用默认条件下并未达成『后台纯净』，认证计划建议但不强求应用在设置中为用户提供开启『后台纯净』模式的选项。最低要求是必须为绿色守护（Greenify）的用户提供开启这一选项的接口。（如果应用默认条件下已达成『后台纯净』，请跳过以下内容）

   由于绿色守护的休眠机制原本就会屏蔽应用的所有后台行为，加入休眠清单的应用，实际上已经丧失了后台执行的能力（包括推送通知），以及相应可产生的UV。而如果应用确保了后台纯净并符合公约要求，则绿色守护不会建议用户将该应用加入休眠清单，即便用户主动将其加入，也默认不会休眠此应用。应用通过提供这一选项，可与用户之间达成和解，从而赢得用户的信任，换取受控的后台执行能力（如`JobScheduler`）。

   如果已在应用自身的设置内提供『后台纯净』的选项，请为应用内对应的设置界面新增一个`<activity-alias>`，包含响应上述`action`的`<intent-filter>`：

   ```
   <activity-alias … android:excludeFromRecents="true">
     <intent-filter>
       <action android:name="com.oasisfeng.greenify.intent.action.REQUEST_LIMITED_BACKGROUND" />
       <category android:name="android.intent.category.DEFAULT" />
     </intent-filter>
   </activity-alias>
   ```
   如果应用不希望在自身的设置界面中提供上述选项，建议仅在通过上述`action`启动设置界面时，显示『后台纯净』的选项（直接打开设置界面时隐藏此选项）。当用户开启后台纯净模式后，后续进入设置界面则始终显示此选项，以便于用户在必要时关闭后台纯净模式。

   绿色守护会在用户将应用加入休眠清单后提示用户该应用提供『后台纯净』选项，通过`startActivityForResult()`启动上述`Activity`。用户确认开启『后台纯净』选项后，应用需要确保完成以下几点：

   * 在界面关闭前通过`setResult()`向绿色守护返回用户的确认结果。（开启为`RESULT_OK`，放弃为`RESULT_CANCEL`）
   * 通过`PackageManager`禁用前述`Activity` (或`activity-alias`），此禁用状态作为绿色守护后续识别『后台纯净』模式已开启的标识。如果用户此后在应用的设置中关闭了『后台纯净』模式，则须通过`PackageManager`重新启用前述`<activity-alias>`。
   * 不启动任何将在后台保持持续运行的服务（`Service`），除非应用处于『前台』状态。
   * 不再初始化会启动后台持续运行服务的三方SDK。
   * 如果应用没有在设置中为所有用户提供开启『后台纯净』模式的选项，则建议当用户已通过绿色守护开启应用的『后台纯净』模式后，在应用自己的设置界面中提供关闭『后台纯净』模式的选项。

# 提交认证

请首先确认应用中已包含上述『认证要求 5』中注明的响应`REQUEST_LIMITED_BACKGROUND`的`<activity-alias>`（未来版本中将移除此项要求，如果你的应用默认满足后台纯净，请在完成自验后从应用中移除此`<activity-alias>`），然后使用[最新版本(3.4.2以上)的绿色守护](http://www.coolapk.com/apk/com.oasisfeng.greenify)进行自验：

打开绿色守护，点击『+』按钮，选择待认证的应用（通常需要展开『其它应用』后才能找到）添加至绿色守护中。在列表中通过 **长按** 选中待认证的应用，然后点击右上方三个小圆点图标展开菜单，选择其中的『Check certification fulfillment』。如果初步通过认证要求，则会提示『All pass』，否则将提示未符合认证的具体原因，或还需要自行确认的关注点。

自验通过后，请在[GitHub issue tracker 提交认证申请](https://github.com/green-android/certification/issues/new?template=----.md&title=[%E8%AE%A4%E8%AF%81%E7%94%B3%E8%AF%B7]%20%E8%AF%B7%E5%A1%AB%E5%86%99%E5%BA%94%E7%94%A8%E5%90%8D)

现阶段认证将以人工审核的形式进行。为降低审核成本，提交认证的应用 **须在单一应用市场至少达到1万的下载量。满足公约中建议条款的应用将获得优先推荐。**

# 认证披露

提交认证前，应用发布方可在应用的相关信息披露（包括应用内界面）中提及『遵循《Android绿色应用公约》(Comply to "Convention of Green Apps for Android")』，但只有在提交认证并审核通过后才允许提及『遵循绿色应用公约，并通过认证(Comply to "Convention of Green Apps for Android", certified)』。链接请一律指向 https://green-android.org/ 。

# 认证有效性

对应用的认证针对应用具体的版本，上述认证要求必须在任何渠道发布的应用包中得到保证。在通过认证后，应用的后续版本须确保继续符合认证要求，否则将失去认证。

此认证计划的要求将会顺应整体生态的发展不断优化调整，通过认证的应用须保持就认证要求的顺畅沟通渠道（至少一名直接负责实施的技术接口人，通过提交认证时提供的联系方式），如果无法跟进认证要求的关键性调整，将保留取消认证的权力。
