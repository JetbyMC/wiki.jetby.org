---
name: Advanced Commands
---

# AdvancedCommand

### [Extend the class](./#extend-the-class)

```java
public class TestCommand extends AdvancedCommand {

    public TestCommand(JavaPlugin plugin) {
        super("test_command", plugin);
    }
}
```

`"test_command"` is the name of the command on the server.

If you need to handle this command, use **`onExecute`**. Importantly, do **not** use `onCommand`, as it is an integral part of the utility's core logic. Modify this **only** if you know exactly what you are doing. The same applies to `onTabComplete`; **instead**, use `onTab`.

#### [onExecute usage:](./#onexecute-usage)

```java
public class TestCommand extends AdvancedCommand {

    public TestCommand(JavaPlugin plugin) {
        super("test_command", plugin);
    }
    @Override
    public boolean onExecute(CommandSender sender, Command command, String label, String[] args) {
        sender.sendMessage("Success");
        return true;
    }
}
```

#### [onTab usage](./#ontab-usage)

```java
public class TestCommand extends AdvancedCommand {

    public TestCommand(JavaPlugin plugin) {
        super("test_command", plugin);
    }
    @Override
    public List<String> onTab(CommandSender sender, Command command, String label, String[] args) {
        return List.of("help");
    }
}
```

#### [Or you can use both:](./#or-you-can-use-both)

```java
public class TestCommand extends AdvancedCommand {

    public TestCommand(JavaPlugin plugin) {
        super("test_command", plugin);
    }
    @Override
    public boolean onExecute(CommandSender sender, Command command, String label, String[] args) {
        sender.sendMessage("Success");
        return true;
    }
    @Override
    public List<String> onTab(CommandSender sender, Command command, String label, String[] args) {
        return List.of("help");
    }
}
```

### [Register](./#register)

```java
new TestCommand(this).register();
```

### [Register with sub commands](./#register-with-sub-commands)

```java
new TestCommand(this)
.addSubCommand(new TestSubCommand())
.addSubCommand(new TestSubCommand2()) // etc
// or
.register();
```

### [Register with sub commands (List)](./#register-with-sub-commands-list)

```java
List<Object> subs = new ArrayList<>();
subs.add(new ShopSubCommand());
subs.add(new MenuSubCommand());
subs.add(new HelpSubCommand());
subs.add(new SettingsSubCommand());

new TestCommand(this).addSubCommand(subs).register();
```
