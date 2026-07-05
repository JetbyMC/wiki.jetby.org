---
name: SubCommand Usage
---

# Sub Command usage

### [Method parameters](sub-command-usage.md#method-parameters)

The first `Player` or `CommandSender` parameter is always injected automatically as the sender — it never consumes an argument.

Every parameter after that maps to the next argument the player types, in order.

```java
@SubCommand({"give"})
public void give(Player sender, Player target, int amount, String reason) {
    // /cmd give <target> <amount> <reason>
}
```

***

#### [Supported types](sub-command-usage.md#supported-types)

**`CommandSender`** — the sender, injected automatically.

```java
public void info(CommandSender sender) {}
```

**`Player` (first param)** — the sender cast to Player. Use with `@PlayerOnly`.

```java
@PlayerOnly
public void home(Player sender) {}
```

**`Player` (not first)** — looks up an online player by name from args.

```java
public void teleport(Player sender, Player target) {}
// /cmd teleport <target>
```

**`String`** — takes one argument as-is.

```java
public void rename(Player sender, String name) {}
// /cmd rename <name>
```

**`String[]`** — consumes all remaining arguments.

```java
public void broadcast(CommandSender sender, String[] message) {}
// /cmd broadcast <word1> <word2> <word3> ...
```

**`int` / `Integer`** — parses a whole number.

```java
public void give(Player sender, int amount) {}
// /cmd give <amount>
```

**`double` / `Double`** — parses a decimal number.

```java
public void speed(Player sender, double value) {}
// /cmd speed <value>
```

**`boolean` / `Boolean`** — accepts `true`/`false` or `yes`/`no`.

```java
public void toggle(Player sender, boolean state) {}
// /cmd toggle <true|false>
```

***

#### [Custom error messages](sub-command-usage.md#custom-error-messages)

Use `@Arg` on any parameter to override the default error message. The placeholder `{input}` is replaced with what the player typed.

```java
@SubCommand({"give"})
@InsufficientArgs("<red>Usage: /cmd give <player> <amount>") // MINI MESSAGE SUPPORT
public void give(
    Player sender, 
    @Arg(error = "Player '{input}' is not online.") Player target,
    @Arg(error = "'{input}' is not a valid number.")  int amount
) {}
```

If `@Arg` is not present, a default message is used. If `@InsufficientArgs` is not present, `"Insufficient arguments."` is shown.

***

### [Annotations](sub-command-usage.md#annotations)

#### `@Permission`

Restricts the subcommand to players with a specific permission node. If the sender lacks it, a message is sent and execution stops.

```java
@SubCommand({"set"})
@Permission("cmd.set")
public void set(Player sender, String value) {}
```

Custom message:

```java
@SubCommand({"set"})
@Permission(value = "cmd.set", message = "You don't have permission to use this.")
public void set(Player sender, String value) {}
```

***

#### `@PlayerOnly`

Blocks console from executing the subcommand.

```java
@SubCommand({"home"})
@PlayerOnly
public void home(Player sender) {}
```

Custom message:

```java
@SubCommand({"home"})
@PlayerOnly(message = "This command is for players only.")
public void home(Player sender) {}
```

***

#### `@Cooldown`

Prevents a player from executing the subcommand again until the cooldown expires. The placeholder `{remaining}` is replaced with seconds left.

```java
@SubCommand({"tp"})
@Cooldown(seconds = 10)
public void tp(Player sender, Player target) {}
```

Custom message:

```java
@SubCommand({"tp"})
@Cooldown(seconds = 10, message = "Wait {remaining}s before using this again.")
public void tp(Player sender, Player target) {}
```

***

#### [Multi-argument subcommands](sub-command-usage.md#multi-argument-subcommands)

`@SubCommand` accepts an array defining the full path to the subcommand. Each element is one argument the player types.

```java
@SubCommand({"set", "type"})
@Permission(value = "cmd.set", message = "You don't have permission.")
@PlayerOnly(message = "Players only command.")
@InsufficientArgs("<red>Usage: /cmd <white>set type <type>")
public void setType(Player sender, String type) {
    sender.sendMessage("Type: " + type);
}
```

This handles `/cmd set type <type>`. The path `{"set", "type"}` is consumed by the router — `type` in the method signature maps to whatever comes after.

***

#### `@TabComplete`

Provides suggestions for a subcommand. The path in `@TabComplete` must match the path in `@SubCommand` exactly.

Single-level:

```java
@TabComplete({"type"})
public List<String> tabType(CommandSender sender, String[] args) {
    return List.of("VILLAGE", "DUNGEON", "CASTLE");
}
```

Multi-level — matches `@SubCommand({"set", "type"})`:

```java
@TabComplete({"set", "type"})
public List<String> tabSetType(CommandSender sender, String[] args) {
    return List.of("VILLAGE", "DUNGEON", "CASTLE");
}
```

The `args` parameter contains everything the player typed after the subcommand path, so you can provide dynamic suggestions based on previous arguments:

```java
@TabComplete({"give"})
public List<String> tabGive(CommandSender sender, String[] args) {
    if (args.length == 1) {
        return Bukkit.getOnlinePlayers().stream()
                .map(Player::getName)
                .collect(Collectors.toList());
    }
    if (args.length == 2) {
        return List.of("1", "16", "32", "64");
    }
    return List.of();
}
```
