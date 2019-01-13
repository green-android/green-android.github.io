# Android 绿色应用公约 3.0（2019 年 1 月）

## 宗旨

这是一项旨在推动 Android 生态中的优秀应用共同维护一个更加良性的『设备体验』而发起的开放公约。

**设备体验**：影响效应超出用户与应用进行显性交互的过程之外，在用户感知中属于设备整体性的体验因素的总称。包括设备的安全性、整体流畅性、耗电程度、发热程度等。

由于 Android 系统的设备体验是由设备本身的软硬件及安装在设备中的众多应用所共同影响的，后者的影响往往随着安装的应用数量增长而迅速扩大。这种由应用所造成的外溢性影响，存在着典型的 [『公地悲剧』](http://baike.baidu.com/item/%E5%85%AC%E5%9C%B0%E6%82%B2%E5%89%A7)。安装的众多应用中，某一个应用对于设备体验的损害往往很难被用户直接辨识，以至设备体验问题长期得不到应用开发团队的足够重视。造成的后果间接的由全部应用，乃至整个 Android 生态共同承担。

因此，除了加强用户对于设备体验损害的辨识能力外，有必要推动整个 Android 开发社区以更高的标准优化各自应用的设备体验影响，共同维护一个良性的 Android 生态。

## 开放编撰

此公约的内容修订和扩充面向整个 Android 开发社区，采取开放接纳、充分讨论、积极修订的原则。如果对规约有任何的疑问（包括实施中的困难）和建议，请通过此公约的 [GitHub issue tracker](https://github.com/green-android/green-android.github.io/issues/new?labels=%E7%BB%BF%E8%89%B2%E5%BA%94%E7%94%A8%E5%85%AC%E7%BA%A6&title=[%E5%85%AC%E7%BA%A6]) 提交。

## 核心原则

* 完全遵照 Android 本身的演进方向（包括 [Android O所引入的新变化](https://developer.android.google.cn/preview/behavior-changes.html)），积极引导和协助应用开发团队平滑完成对接 Android 最新变化的节奏，在确保应用核心功能不受影响的前提下，减少不必要的应用后台行为，并以更加高效、节能的调度机制改善后台行为的调度。

* 公约的必要规约中，只纳入可被明确验证的条款，不接受需要主观裁量或定义模糊的条款（例如涉及交互设计的内容）。

* 所有约束条款均给出推荐的最佳实践或具有可操作性的调整方法。

* 涉及到功能与设备体验之间的潜在冲突时，遵循最终选择权给予用户的原则。

## 规约

### 必要部分

1. **Target SDK Version 最低：26**

   原因：这是发挥 Android 新版本部分机制优化和安全设计的关键开关。当应用的 targetSdkVersion 低于设备当前的 Android 版本时，系统会为应用启用兼容模式，通过关闭新版本的部分机制优化和安全设计以确保应用运行的兼容性，这往往是以牺牲设备体验和安全性为代价的。为了消除应用开发者故意滥用低 target 绕过 Android 机制优化和安全设计，Google 已正式启动 Target SDK Version 的退出政策（最低限制）。从 2018 年 8 月开始针对所有在 Google Play 市场发布的新应用要求最低 26（从 11 月开始针对所有的应用更新），并在未来随着 Android 版本的迭代同步提高。相应的，Android P 也开始对低于 17 的应用在启动时弹出警告。

   Android 8 (API 26)：[对应用的后台行为约束进行了大幅度的调整](https://developer.android.google.cn/preview/features/background.html)，取消了应用原本通过静态声明广播接收器所能获得的绝大部分响应系统事件的后台启动能力（俗称『自启动』），并完全限制了应用在后台期间保留其后台服务的能力，从根本上杜绝了后台应用异常消耗系统资源的常见途经，有助于大幅度降低应用后台行为对设备体验的影响。

   Android 7 (API 24)：[Project Svelte 得到了一些强化](https://developer.android.google.cn/about/versions/nougat/android-7.0-changes.html#bg-opt)，确保过于频繁的系统事件不再唤醒大量应用的后台，有助于降低一些场景下（如拍照、网络切换）设备出现的间歇性卡顿。

   附：Google 官方的 [Target SDK Version 合规指导](https://developer.android.google.cn/distribute/best-practices/develop/target-sdk)

2. **不在启动应用时强制请求『读取手机状态和身份（READ_PHONE_STATE）』权限。**

   原因：IMEI (GSM) / MEID (CDMA) 属于手机及其它具备移动通信功能的设备中不可变更或重置的唯一标识，同时也是手机在蜂窝网络通信中用以唯一识别终端的关键标识信息。IMEI/MEID 不仅使得广告网络在设备的整个生命周期中实现用户的唯一甄别，还可能被用于蜂窝网络中的设备欺骗攻击，因此 IMEI/MEID 泄露是目前用户隐私和手机安全中的一个突出问题。这一权限的表述也具有相当的迷惑性，在 Android 6.0 之后的运行期权限体系中依然未能获得足够清晰的风险披露。由于 Android 系统仅仅将其显示为『读取手机状态和身份』，使得大部分用户在应用请求此项权限时虽然困惑，但仍未意识到授予这个权限背后存在的安全隐患。

   鉴于越来越多的国家和地区开始实施更为严格的隐私保护政策（如欧盟的 GDPR 条例），尤其是对不可变更或重置的设备唯一标识的跟踪限制，Google 在其应用市场的开发者协议中明确禁止将 IMEI/MEID 等永久唯一标识用于长期识别用户身份，详细说明请参阅 [官方文档](https://developer.android.google.cn/training/articles/user-data-ids.html)。

   若应用中的某些功能（如通话相关的特性）依赖此权限，则只能在对应的功能交互中请求此权限。即便用户拒绝授予权限，不依赖此权限的功能仍须保持可用。

   涉及资金或财产安全的应用（如支付类、电子商务类），如果在安全风控中需要用到 IMEI 等永久唯一标识，可在必要时（非应用启动阶段）请求此项权限，但须向用户提供具有法律效力的用户隐私协议，明确包含针对设备永久唯一标识的使用范围和保护责任的说明。

3. **除用户的主动交互触发外，避免启动其它应用未处于运行中的进程。**

   原因：用户在主动交互中通常对交互的响应时间（例如从触摸到界面变化）存在一定的宽容度，而被动交互（例如启动过程的等待、媒体播放中）中出现的延迟或卡顿更易引发用户的反感。此间如果涉及到启动多个进程，除进程创建本身的显著开销和内存压力之外，如果启动的是其它应用的进程（即通常所说的『交叉唤醒』），对方的初始化开销则是一个完全不可控的因素。而交叉唤醒在应用之间往往具有连锁效应，在安装有较多关联应用（例如集成了相同 SDK 的多个应用）的情况下极易触发『链式唤醒』，引发 CPU、内存、IO 等资源短时间内的巨大压力，造成设备流畅性的急剧下降、耗电上升，带来严重的应用启动阶段用户体验和全局设备体验的双重损害。

   如果观察到（或怀疑）使用的第三方闭源 SDK 存在上述交叉唤醒行为，建议接入轻量的开源辅助库 [Project Condom](https://github.com/oasisfeng/condom)，以识别和消除这类交叉唤醒。

4. **使用请求唤醒 CPU 的周期性任务（如 Alarm、JobScheduler、Sync Adapter）时，其周期建议不低于 1 小时，最小不低于 30 分钟，并避免在不必要的时间段（如夜间）继续调度周期性事件。间隔低于 12 小时的周期性任务，必须提供可关闭的选项。**

   原因：周期性唤醒 CPU 会打断设备的深度睡眠状态，造成设备待机时长的明显缩短。按照 Google 在 Project Volta 中的粗略测算，设备每1秒钟的活跃工作会让待机时间损失大约 2 分钟。大部分应用的后台周期性任务往往以网络访问为主，通常会持续数秒至数十秒（甚至超过 1 分钟）。如果此类周期性后台活动调度过于频繁，对待机时间的影响极其显著。 Android 从 4.4 开始，不断在迭代中优化周期任务的后台调度，但所有这些努力都只能在长周期任务中产生明显的效果。倘若有一个应用请求过于频密的周期任务，则整个系统的待机时长就会因为短木桶效应而受制。

5. **在 Android 5.0 及以上版本的设备中，避免使用『读取/写入外部存储（READ / WRITE_EXTERNAL_STORAGE）』权限。**（豁免：仅限文件管理类应用）

   原因：外部存储通常是用户私人照片、视频的保存位置，涉及用户的敏感隐私。除文件管理类工具，应尽可能避免使用此权限。

   Android 设备现已普遍采用虚拟分区，内部存储和外部存储（External Storage）实际上共享的是相同的物理存储位置和配额，因此不必担心存储空间内部比外部存储更容易耗尽。

   如果确有需要将应用的数据（或缓存）存入外部存储，或读写其它应用写入外部存储的数据，则需分“用户个人资料（如图片、文档）”、“应用私有数据”和“其它应用数据”三种情形分别应对：

   * **用户个人资料**：如果仅仅是为了方便用户导出图片、视频、音频等媒体文件，供其它应用（比如 微信）读取，建议使用 Android 5.0 新增的 API - `Context.getExternalMediaDirs()`。存储在此位置的文件，应用自身无需存储权限即可读写，而其它应用可通过 `MediaStore` 或者直接访问（需存储权限），用户还可以通过文件管理器方便访问。

     > 如果应用需要兼容 Android 4.4 及以下版本，请以版本上限的方式声明外部存储权限，并在旧版本系统上直接读写外部存储。
     >
     > `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" android:maxSdkVersion="20" />`

     如果希望由用户自由决定文件存储的位置，可使用 Android 4.4 引入的“[存储访问框架（Storage Access Framework）](https://developer.android.google.cn/guide/topics/providers/document-provider.html#client)”，实现用简单的 API 和通用交互（类似于 Windows 下打开 / 保存文件时使用的标准对话框）无缝对接各种本地存储介质（如 TF 卡、USB OTG 外置存储、NAS）及第三方云存储服务，为用户提供非常灵活的存取选择。

     > 如果应用需要兼容 Android 4.3 及以下版本，请以版本上限的方式声明外部存储权限，并在旧版本系统上直接读写外部存储。
     >
     > `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" android:maxSdkVersion="18" />`

     如果需要对用户选定的文件或位置进行长期的文件读写（例如自动备份），可使用 Android 5.0 及以上版本提供的 API：[`ContentResolver.takePersistableUriPermission()`](https://developer.android.google.cn/reference/android/content/ContentResolver.html#takePersistableUriPermission(android.net.Uri,%20int))

   * **应用私有数据**：通常不建议写入外部存储，因为外部存储可被其它应用访问，存在数据安全风险，这意味着通常还需要对涉及用户隐私的数据额外加密保存。如果确有特殊原因需要将数据写入外部存储，[`Context.getExternalFilesDir()`](https://developer.android.google.cn/reference/android/content/Context.html#getExternalFilesDir(java.lang.String))、[Context.getExternalCacheDir()](https://developer.android.google.cn/reference/android/content/Context.html#getExternalCacheDir()) 等相关 API 所返回的路径 [从Android 4.4开始可供应用直接存取，无需任何权限](https://developer.android.google.cn/reference/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE)。

     > 如果应用需要兼容 Android 4.3 及以下版本，请以版本上限的方式声明外部存储权限，并在旧版本系统上直接读写外部存储。
     >
     > `<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" android:maxSdkVersion="18" />`

   * **其它应用数据**：常规应用不能访问其它应用保存在内部存储中的私有数据，但可以在用户的显式授权下访问其它应用保存在外部存储中的数据文件（或整个文件夹）。具体操作方式与上述“用户个人资料”类似，可以在请求 `ACTION_OPEN_DOCUMENT` 时添加 [`DocumentsContract.EXTRA_INITIAL_URI`](https://developer.android.google.cn/reference/android/provider/DocumentsContract.html#EXTRA_INITIAL_URI) 给出默认路径引导用户选择对应的位置。

### 建议部分

1. **上架 Google Play 应用市场**

   Google Play 应用市场（以下简称 Google Play）是 Android 生态中全球最大的应用分发渠道，在除中国大陆地区外发售的绝大部分 Android 手机中是预装的唯一应用市场。由于 Google Play 在国内的 Android 应用分发渠道中并未获得主导地位，但这并不妨碍应用开发者应将应用上架 Google Play 的重要性。将应用上架 Google Play 可获得如下优势：

   * **避免“应用唯一标识（App ID）”被恶意抢注，成为未来国际化道路上的“过失性障碍”。** （重要性类似于域名注册）
   * **及早在 Google Play 市场中抢占竞争优势。** 由于因为在 Google Play 上积累口碑和评价远比国内的应用市场严格和困难，在竞争对手尚未觉察到这一点前，投入少量的精力（增加一个分发渠道）即可换取潜在的高回报，避免启动国际化战略之后面临被动局面。
   * **接轨 Google Play 市场的要求、充分利用其提供的工具和服务，可以让开发团队及早完成与国际主流技术的对接，降低未来国际化的门槛和阻力。**
