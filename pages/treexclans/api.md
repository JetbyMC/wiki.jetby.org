# API

{% tabs %}
{% tab title="Gradle" %}
```css
repositories {
    maven {
        url "http://api.jetby.org/"
        name "JetbyMC"
    }
}

dependencies {
    compileOnly "org.jetby:treexclans:api:VERSION"
}
```
{% endtab %}

{% tab title="Maven" %}
```xml
<repository>
  <id>jJetbyMC</id>
  <url>http://api.jetby.org/</url>
</repository>

<dependency>
  <groupId>org.jetby.treexclans</groupId>
  <artifactId>api</artifactId>
  <version>VERSION</version>
  <scope>provided</scope>
</dependency>
```
{% endtab %}
{% endtabs %}

{% stepper %}
{% step %}
### Get started



First of all, you have to make main class.\
Your main class you have the implementaion `JavaAddon` and annotation `ClanAddon()`\
\
**Example:**

```java
@ClanAddon(
        id = "MyAddon", // required
        version = "1.0"  // required
)
public class MyAddon extends JavaAddon {}
```

So then, you can override your `onEnable` and `onDisable` methods.\
\
**Example:**

```java
@ClanAddon(
        id = "MyAddon",
        version = "1.0"
)
public class MyAddon extends JavaAddon {

    @Override
    public void onEnable() {
    }

    @Override
    public void onDisable() {
    }
}
```

Congrats, you addon is ready to start.&#x20;
{% endstep %}

{% step %}
### API

To get an instance of this API use:

```java
TreexClansAPI.get()
```

#### The instance includes itself:

```java
@NotNull Economy getEconomy();
CommandService getCommandService();
JavaPlugin getPlugin();
EventRegistrar getEventRegistrar();
AddonManager getAddonManager();
@NotNull ClanManager getClanManager();
```
{% endstep %}

{% step %}
### Learn more

[https://github.com/JetbyMC/TreexClansV3/tree/master/api](https://github.com/JetbyMC/TreexClansV3/tree/master/api)
{% endstep %}
{% endstepper %}
