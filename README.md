# tos-app-dufs ✅ 已解封并 VM 验证(18242)(2026-11-20 VM 实测认证规则跑通)

将 [dufs](https://github.com/sigoden/dufs)(轻量文件服务器 + WebDAV,Apache-2.0/MIT 双许可)打包为 [铁威马 TOS](https://www.terra-master.com) 应用中心 **deb 类应用**(x86_64 + aarch64 双架构)。

## ✅ 解封记录(2026-11-20)

**VM 实测两坑均已修复:**
1. `--auth dufs:PASS@/:rw,a` 格式正确(VM 实机 200,凭据拒绝时 401);
2. serve root `/Volume1/public` 属主是 twmtest,btrfs `tmacl` 挂载选项拒绝 dufs 用户读——**postinst 已自动 chown 共享目录给 dufs 用户**。

---

## 应用概要(解封后有效)

| 项目 | 值 |
|---|---|
| 应用 ID | `dufs` |
| 应用形态 | deb 类 · open_path 外开 |
| Web UI | `http://<NAS>:18242`(浏览/上传/下载/编辑/WebDAV,basic auth 首装生成) |
| 共享目录 | `/Volume1/public`(env 可改) |
| 版本 | 0.47.0 musl 静态双架构(UPSTREAM 锁定) |
| 上游许可证 | Apache-2.0/MIT 双许可(LICENSE + LICENSE-MIT 随包) |

## 本地构建

依赖:bash、curl、python3。

```bash
./build.sh                # 双架构(tarball → 校验 → 打包 → 解包验证)
./scripts/validate.py     # 元数据校验
```

产物:`build/output/dufs_<platform>.deb` + `.sha256`(约 1.4MB,全场最小)。

## 上架 Checklist(解封后)

1. ☐ 修复 basic-auth 规则格式(见上),重打包;
2. ☐ 刷新查重(`dufs`,2026-11-16 核验空白,但文件服务器品类拥挤);
3. ☐ x86_64 与 ARM 分别创建应用;
4. ☐ 提交 Release 直链 + SHA256 + 上游源码仓 + 本仓构建脚本;
5. ☐ VM 实测:浏览器登录后上传/下载/删除截图;
6. ☐ 30 天内维护 Issues 响应。

## 合规声明

- 上游二进制**原样封装**(Apache-2.0/MIT),未修改任何上游代码,双许可全文随包分发;
- 安装包内容:上游 tarball 二进制 + 本仓元数据,无其他二进制;
- 不收集任何用户数据。
