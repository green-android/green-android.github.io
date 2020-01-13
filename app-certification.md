# 绿色应用认证计划

为推广和促进[《绿色应用公约》](app-convention.html)在国内 Android 应用生态中的普遍接纳，推动更多有责任感的开发团队积极加入改善 Android 设备体验的行列，[绿色守护（Greenify）](http://www.coolapk.com/apk/com.oasisfeng.greenify)联合国内主流的科技媒体、应用社区和传播渠道共同推出绿色应用认证计划，加大在普通用户群体中对设备体验的科普教育，并对遵守公约捍卫设备体验的优秀应用进行宣传推广，促进从用户、应用开发团队到设备厂商对公约所提倡的设备体验原则的普遍认同，弥合整个生态中日渐分裂的应用后台行为和限制约束。

通过认证的应用，将有机会获得在公约网站及相关媒体、宣传渠道的推广。 **在应用中添加『已通过《Android 绿色应用公约》认证』信息（通常在『关于』或『设置』界面中），并链接到公约官方网站的应用，将获得更靠前的推广位次。** （请在认证申请 issue 中附上截图）

# 认证要求

针对国内的复杂国情（尤其是推送渠道的碎片化问题），以维护应用的合理利益为出发点，在《绿色应用公约》的基础上，补充以下指引：

1. 公约中的第1点要求仅约束应用在 `AndroidManifest.xml` 中声明的 `targetSdkVersion` 属性，对 `minSdkVersion` 属性和开发中使用的 SDK 版本无要求。开发团队须自行确保应用符合 [Android系统本身对`targetSdkVersion`的约束要求](https://developer.android.google.cn/reference/android/os/Build.VERSION_CODES.html#N)。

2. 针对公约中的第2点要求，可能有部分三方 SDK 要求必须在 `AndroidManifest.xml` 中声明 `READ_PHONE_STATE` 权限，否则拒绝工作。 **解决方法是保留权限声明，但不在运行期请求此项权限。**

   经过与相关 SDK 开发团队的沟通，统计和 Push 类 SDK 其实并不依赖这一权限，因为一方面不含基带的 Android 设备（如大部分平板电脑）都没有 IMEI，另一方面 Android 10 已彻底屏蔽了对 IMEI 的读取，所以三方 SDK 的实现中都不会强依赖 IMEI。

3. 针对公约中的第 3 点要求，如果应用中集成了国内的第三方 SDK，则需要评估其是否存在『交叉唤醒』行为（典型如国内的大部分推送 SDK）。 **建议接入轻量的开源辅助库 [Project Condom](https://github.com/oasisfeng/condom)，识别和消除第三方 SDK 造成的交叉唤醒。**

4. 针对公约中的第 4 点要求，请通过 `dumpsys alarm | grep <package name>` 和 `dumpsys jobscheduler <package name>` 完成自查。

5. 针对公约中的第 5 点要求，除非设备适配的需要（认证申请中需具体说明），非文件管理（含文件清理）类应用必须确保在 Android 5.0 及以上版本中无「读取/写入外部存储」权限声明。（允许以 `<uses-permission ... android:maxSdkVersion="20" />` 方式针对 Android 4.x 版本继续请求上述权限）

   如果使用到的第三方 SDK 强制要求声明上述权限，则允许仅在 AndroidManifest.xml 中声明，但不得在运行期请求上述权限。认证申请中需要列出提出此项强制要求的第三方 SDK。

# 提交认证

请首先确认应用已完全符合上述 5 项条款的要求，然后使用 [最新版本(3.4.2以上)的绿色守护](http://www.coolapk.com/apk/com.oasisfeng.greenify) 进行自验：

首先确认设备已开启了「开发者选项」，然后打开绿色守护，点击『+』按钮，选择待认证的应用（通常需要展开『其它应用』后才能找到）添加至绿色守护中。在列表中通过 **长按** 选中待认证的应用，然后点击右上方三个小圆点图标展开菜单，选择其中的『Check certification fulfillment』。如果初步通过认证要求，则会提示『All pass』，否则将提示未符合认证的具体原因，或还需要自行确认的关注点。

自验通过后，请在[GitHub issue tracker 提交认证申请](https://github.com/green-android/certification/issues/new?template=----.md&title=[%E8%AE%A4%E8%AF%81%E7%94%B3%E8%AF%B7]%20%E8%AF%B7%E5%A1%AB%E5%86%99%E5%BA%94%E7%94%A8%E5%90%8D)

现阶段认证将以人工审核的形式进行。为降低审核成本，提交认证的应用 **须在单一应用市场至少达到1万的下载量。满足公约中建议条款的应用将获得优先推荐。**

# 认证披露

提交认证前，应用发布方可在应用的相关信息披露（包括应用内界面）中提及『遵循《Android绿色应用公约》(Comply to "Convention of Green Apps for Android")』，但只有在提交认证并审核通过后才允许提及『遵循绿色应用公约，并通过认证(Comply to "Convention of Green Apps for Android", certified)』。链接请一律指向 https://green-android.org/ 。

# 认证有效性

对应用的认证针对应用具体的版本，上述认证要求必须在任何渠道发布的应用包中得到保证。在通过认证后，应用的后续版本须确保继续符合认证要求，否则将失去认证。

此认证计划的要求将会顺应整体生态的发展不断优化调整，通过认证的应用须保持就认证要求的顺畅沟通渠道（至少一名直接负责实施的技术接口人，通过提交认证时提供的联系方式），如果无法跟进认证要求的关键性调整，将保留取消认证的权力。
